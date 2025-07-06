# agents/tools/cve_lookup.py

import requests
import os
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
NVD_API_KEY = os.getenv("NVD_API_KEY")
print("🔐 Using NVD API Key:", NVD_API_KEY)

BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

def lookup_cve(cve_id):
    headers = {}
    if NVD_API_KEY:
        headers['apiKey'] = NVD_API_KEY

    params = {"cveId": cve_id}
    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code != 200:
        return f"❌ Failed to fetch CVE: {cve_id}. Status: {response.status_code}"

    data = response.json()
    print("DEBUG: Full response JSON:", data)  # For debugging structure

    try:
        vulnerabilities = data.get("vulnerabilities", [])
        if not vulnerabilities:
            return f"⚠️ No data found for {cve_id}"

        cve_data = vulnerabilities[0].get("cve", {})

        descriptions = cve_data.get("descriptions", [])
        description = descriptions[0]["value"] if descriptions else "No description available."

        metrics = cve_data.get("metrics", {})
        cvss = {}
        if "cvssMetricV31" in metrics:
            cvss = metrics["cvssMetricV31"][0].get("cvssData", {})
        elif "cvssMetricV2" in metrics:
            cvss = metrics["cvssMetricV2"][0].get("cvssData", {})

        severity = cvss.get("baseSeverity", "Unknown")
        score = cvss.get("baseScore", "N/A")

        references = cve_data.get("references", [])
        ref_urls = [ref.get("url") for ref in references[:3]]

        return {
            "cve_id": cve_id,
            "description": description,
            "severity": severity,
            "cvss_score": score,
            "references": ref_urls
        }

    except Exception as e:
        return f"⚠️ Error parsing CVE response: {str(e)}"

# Example test run
if __name__ == "__main__":
    cve_id = "CVE-2019-1010218"
    result = lookup_cve(cve_id)
    from rich import print
    print(result)
