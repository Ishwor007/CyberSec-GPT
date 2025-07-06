from langchain.tools import BaseTool
from agents.tools.cve_lookup import lookup_cve

class CVELookupTool(BaseTool):
    name: str = "cve_lookup"
    description: str = "Look up CVE details by ID."

    def _run(self, cve_id: str) -> str:
        return str(lookup_cve(cve_id))

    async def _arun(self, cve_id: str) -> str:
        raise NotImplementedError()
