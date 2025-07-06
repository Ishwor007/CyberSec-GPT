# agents/tools/nmap_live_scan.py

import subprocess
import os
import tempfile
from agents.tools.nmap_parser import parse_nmap_xml

def run_nmap_scan(subnet: str) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xml") as temp_file:
        output_path = temp_file.name

    try:
        # Runs a basic ping scan and saves output to XML
        print(f"📡 Scanning subnet: {subnet}")
        subprocess.run(["nmap", "-T4", "-oX", output_path, subnet], check=True)

        # Parse the resulting XML file
        result = parse_nmap_xml(output_path)
        os.remove(output_path)  # Clean up
        return result
    except subprocess.CalledProcessError as e:
        return f"❌ Error running Nmap: {e}"
    except Exception as ex:
        return f"❌ Unexpected error: {ex}"
