from langchain.tools import BaseTool
from typing import Optional
from agents.tools.nmap_parser import parse_nmap_xml

class NmapParserTool(BaseTool):
    name: str = "nmap_parser"
    description: str = "Parses Nmap XML scan file and summarizes the open ports and services."

    def _run(self, file_path: str) -> str:
        try:
            summary = parse_nmap_xml(file_path)
            return str(summary)
        except Exception as e:
            return f"Error parsing Nmap XML: {e}"

    async def _arun(self, file_path: str) -> str:
        # Async not implemented for now
        raise NotImplementedError("NmapParserTool does not support async")
