# agents/tools/nmap_parser.py

import os
import xml.etree.ElementTree as ET

def parse_nmap_xml(xml_path):
    """
    Parses an Nmap XML output file and summarizes scan results.

    Args:
        xml_path (str): Path to the Nmap XML file.

    Returns:
        list: Summary list with hosts info, open ports, services, etc.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    hosts_summary = []

    for host in root.findall('host'):
        status = host.find('status').get('state')
        addresses = [addr.get('addr') for addr in host.findall('address')]
        host_info = {
            "status": status,
            "addresses": addresses,
            "ports": []
        }

        ports = host.find('ports')
        if ports is not None:
            for port in ports.findall('port'):
                port_id = port.get('portid')
                protocol = port.get('protocol')
                state = port.find('state').get('state')
                service = port.find('service').get('name') if port.find('service') is not None else "unknown"

                host_info['ports'].append({
                    "port": port_id,
                    "protocol": protocol,
                    "state": state,
                    "service": service
                })

        hosts_summary.append(host_info)

    return hosts_summary

if __name__ == "__main__":
    # Get current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Build full path to sample_nmap.xml in the same folder
    xml_file = os.path.join(script_dir, "sample_nmap.xml")

    summary = parse_nmap_xml(xml_file)

    from rich import print
    print(summary)
