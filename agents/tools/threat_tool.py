# agents/tools/threat_tool.py

from langchain.tools import BaseTool
from agents.tools.threat_detector import detect_threats
import json

class ThreatDetectionTool(BaseTool):
    name: str = "threat_detector"
    description: str = "Analyzes scan summaries and detects threats, suggests remediations."

    def _run(self, json_summary: str) -> str:
        try:
            parsed = json.loads(json_summary)
            return detect_threats(parsed)
        except Exception as e:
            return f"❌ Error in threat detection: {e}"

    async def _arun(self, json_summary: str) -> str:
        raise NotImplementedError()
