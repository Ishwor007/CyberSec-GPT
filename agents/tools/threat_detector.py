# agents/tools/threat_detector.py

# Mapping port/services to MITRE and suggestions
THREAT_DB = {
    22: {
        "technique": "T1110 - Brute Force",
        "description": "Repeated SSH login attempts may indicate brute force attacks.",
        "suggestion": "Enable rate-limiting, use SSH key auth, and fail2ban."
    },
    3389: {
        "technique": "T1021 - Remote Services",
        "description": "RDP exposed to the internet can be exploited.",
        "suggestion": "Restrict access via firewall or VPN, enable NLA, monitor login attempts."
    },
    23: {
        "technique": "T1046 - Telnet Discovery",
        "description": "Telnet is insecure and often targeted.",
        "suggestion": "Disable Telnet and replace with SSH."
    },
    445: {
        "technique": "T1071 - SMB Communication",
        "description": "SMB can be used for lateral movement.",
        "suggestion": "Block SMB externally, segment networks."
    }
}

def detect_threats(scan_summary: list) -> str:
    results = []

    for host in scan_summary:
        ip = ", ".join(host.get("addresses", []))
        open_ports = host.get("ports", [])
        for port_info in open_ports:
            port = int(port_info.get("port", -1))
            if port in THREAT_DB:
                entry = THREAT_DB[port]
                results.append(f"""
🔍 Host: {ip}
⚠️  Port: {port}
🧠 Technique: {entry['technique']}
📄 Description: {entry['description']}
✅ Suggestion: {entry['suggestion']}
""")
    if not results:
        return "✅ No high-risk services detected."
    return "\n".join(results)
