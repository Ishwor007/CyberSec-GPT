from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from tools.nmap_tool import NmapParserTool
from tools.cve_lookup_tool import CVELookupTool  # your CVE tool wrapped similarly

def main():
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    tools = [NmapParserTool(), CVELookupTool()]

    agent = initialize_agent(tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True)

    print("CyberSec-GPT Agent started. Type 'exit' to quit.")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        output = agent.run(user_input)
        print("Agent:", output)

if __name__ == "__main__":
    main()
