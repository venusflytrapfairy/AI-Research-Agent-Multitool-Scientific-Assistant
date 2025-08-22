# AI-Research-Agent-Multitool-Scientific-Assistant
A Python-based AI agent designed for dynamic research assistance. Powered by Google Vertex AI's Gemini LLM and LangChain integration, this agent intelligently combines web search, Wikipedia summarization, and automated file saving into a smooth workflow. 
## Features

- **Multi-tool orchestration:** Combines web search, Wikipedia query, and save-to-file capabilities intelligently
- **Powered by Google Vertex AI Gemini:** Uses Google’s latest Gemini 2.5 Pro LLM for natural language understanding and generation
- **Structured output:** Returns research summaries in a clean, predefined schema for easy consumption or further automation
- **Environment ready:** Leverages `.env` for secure, flexible configuration of Google Cloud credentials and parameters
- **Interactive CLI:** Query the agent via a simple command-line interface, with verbose tool execution logging
- **Extendable toolset:** Modular tooling makes it easy to add more information sources or capabilities

## How It Works

The agent receives a user query and decides which tools to invoke to retrieve relevant information. It first queries Wikipedia or web search tools to generate a concise, source-backed summary. If asked, it can save the information to a structured text file with timestamps. All responses conform to a Pydantic schema for consistency.

## Getting Started

### Prerequisites

- Python 3.9+
- Google Cloud account with Vertex AI and appropriate credentials
- Required Python packages listed in `requirements.txt`

### Installation

1. Clone this repository:
git clone https://github.com/yourusername/ai-research-agent.git
cd ai-research-agent

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt


4. Configure environment variables in `.env`:
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
GOOGLE_PROJECT=your-google-project-id
GOOGLE_REGION=your-google-region


### Usage

Run the main script:
python main.py

text

Enter your research query. You can also instruct the agent to save results to a file by including that in your query, e.g.:

research about the population of south asia, save to a file


### Output

The agent returns a JSON-formatted structured response with:

- **topic:** The main research topic
- **summary:** A concise summary of research findings
- **sources:** URLs or references used for the answer
- **tools_used:** The tools invoked to gather information

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to add new tools, improve prompt engineering, or enhance output formatting.

## License

MIT License © 2025 Anusha Asim

---

Built with ❤️ using Google Vertex AI, LangChain, and Python.
