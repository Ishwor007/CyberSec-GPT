# CyberSec-GPT
# CyberSec-GPT: An Agentic AI for Threat Intelligence and Incident Response

> "Give me logs, CVEs, or commands — and I’ll investigate, summarize, find threats, and suggest actions."

---

## Overview

CyberSec-GPT is an autonomous cybersecurity analyst agent built with LangChain and OpenAI GPT-4. It can:

- Parse raw security logs (Nmap, Suricata, Snort, Zeek, firewall logs, etc.)
- Lookup CVE details using the NVD API
- Analyze scan results and logs to detect threats
- Provide threat summaries, risk scores, and remediation suggestions
- Execute commands like subnet scans and summarize outputs
- Remember past inputs for multi-step reasoning

---

## Features

- **CVE Lookup Tool**: Fetches vulnerability details from the NVD database.
- **Nmap XML Parser Tool**: Parses Nmap scan XML files and summarizes open ports and services.
- **LangChain Agent**: Integrates multiple tools and uses GPT-4 for reasoning and conversational responses.
- **Streamlit UI** (optional): Upload scan files and interact with the agent through a web interface.
- **Memory & Planning**: Agent retains context across interactions for better threat analysis.

---

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API Key
- NVD API Key (optional but recommended for higher rate limits)

### Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/cybersec-gpt.git
cd cybersec-gpt

2. Create and activate a Python virtual environment:

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate


3. Install dependencies:
pip install -r requirements.txt


4. Create a .env file in the root directory with your API keys:

OPENAI_API_KEY=your_openai_api_key_here
NVD_API_KEY=your_nvd_api_key_here




###  Usage


1. Run the CyberSec-GPT Agent (CLI)


python main.py
Type commands like:

Parse the nmap scan at path/to/file.xml
Lookup CVE-2023-34362
Scan the 192.168.1.0/24 subnet and summarize results

Type exit to quit.



2. Run the Streamlit UI (Optional)

streamlit run app.py
Upload your Nmap XML scan files and get parsed summaries in the browser.

Notes
Ensure you have enough quota and billing set up on your OpenAI account.

You can switch models between gpt-3.5-turbo and gpt-4 based on your access.

Contribution
Feel free to open issues or submit pull requests to improve the project.

