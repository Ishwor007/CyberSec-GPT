
# main.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("Missing OPENAI_API_KEY in environment. Add it to your .env file.")

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

# Import your custom tools - adjust paths as per your project
from agents.tools.nmap_tool import NmapParserTool
from agents.tools.cve_lookup_tool import CVELookupTool
from agents.tools.nmap_live_tool import NmapLiveScanTool
from agents.tools.threat_tool import ThreatDetectionTool

def main():
    # Initialize the LLM with your API key
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=openai_api_key)

    # Instantiate your tools
    tools = [
        NmapParserTool(),
        CVELookupTool(),
        NmapLiveScanTool(),
        ThreatDetectionTool(),
    ]

    # Create the agent
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    print("CyberSec-GPT agent ready! Type 'exit' to quit.")
    while True:
        user_input = input("\nEnter command, CVE ID, or logs:\n> ")
        if user_input.lower() in {"exit", "quit"}:
            print("Exiting CyberSec-GPT. Goodbye!")
            break

        try:
            response = agent.run(user_input)
            print("\n[Agent]:", response)
        except Exception as e:
            print(f"Error running agent: {e}")

from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from tools.nmap_tool import NmapParserTool
from tools.cve_lookup_tool import CVELookupTool  # your CVE tool wrapped similarly

if __name__ == "__main__":
    main()
