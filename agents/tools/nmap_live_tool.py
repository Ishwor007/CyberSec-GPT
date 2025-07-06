# agents/tools/nmap_live_tool.py

from langchain.tools import BaseTool
from agents.tools.nmap_live_scan import run_nmap_scan

class NmapLiveScanTool(BaseTool):
    name: str = "nmap_live_scan"
    description: str = "Run a live Nmap subnet scan (e.g., 192.168.1.0/24) and summarize the results."

    def _run(self, subnet: str) -> str:
        return str(run_nmap_scan(subnet))

    async def _arun(self, subnet: str) -> str:
        raise NotImplementedError()
