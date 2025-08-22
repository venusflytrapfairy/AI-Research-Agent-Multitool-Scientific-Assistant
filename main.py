from dotenv import load_dotenv
from pydantic import BaseModel
import os
from langchain_google_vertexai import ChatVertexAI
import vertexai
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool


# Load environment variables from .env file
load_dotenv()

#output structure
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# Read values from environment variables
CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
PROJECT = os.getenv("GOOGLE_PROJECT")
REGION = os.getenv("GOOGLE_REGION")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS

vertexai.init(
    project=PROJECT,
    location=REGION,
)

llm = ChatVertexAI(model="gemini-2.5-pro")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a research assistant that MUST ALWAYS use the search tool to answer ANY query.
After using the tool, you MUST summarize your response *strictly* in the given Python schema and provide no extra text. 
Even if you cannot find information, fill the schema with empty or generic values.
ALWAYS use this format—never leave the output empty!

{format_instructions}
        """
    ),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),
]).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]

agent = create_tool_calling_agent(llm =llm, prompt=prompt, tools=tools)
agent_executor = AgentExecutor(agent = agent, tools = tools, verbose = True)
query = input("What can I help you research?")
raw_response = agent_executor.invoke({"query": query})

try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)