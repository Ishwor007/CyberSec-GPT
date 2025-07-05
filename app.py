import streamlit as st
from agents.tools.nmap_tool import NmapParserTool

st.title("CyberSec-GPT - Nmap Scan Parser")

uploaded_file = st.file_uploader("Upload Nmap XML scan file", type="xml")

if uploaded_file is not None:
    # Save uploaded file temporarily
    temp_path = "temp_scan.xml"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    # Parse and show results
    tool = NmapParserTool()
    result = tool._run(temp_path)

    st.subheader("Parsed Scan Summary")
    st.text(result)
