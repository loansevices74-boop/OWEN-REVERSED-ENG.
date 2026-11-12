"""Streamlit front end for a lightweight REA reverse-engineering workspace."""
from __future__ import annotations

import hashlib

import streamlit as st


st.set_page_config(page_title="REA Reverse Engineering", page_icon="🔬", layout="wide")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


st.title("🔬 REA Reverse Engineering Workspace")
st.caption("A Streamlit starting point for organizing reverse-engineering investigations.")

with st.sidebar:
    st.header("Investigation setup")
    target = st.text_input("Target", placeholder="App URL, binary name, package, or repository")
    objective = st.text_area("Objective", placeholder="What behavior or artifact do you want to understand?", height=120)
    uploaded = st.file_uploader("Evidence or artifact", type=None)
    st.divider()
    st.info("Run locally with: streamlit run app.py")

if not target:
    st.warning("Enter a target in the sidebar to begin an investigation.")

metrics = st.columns(3)
metrics[0].metric("Target", target or "Not set")
metrics[1].metric("Evidence", "Attached" if uploaded else "None")
metrics[2].metric("Status", "Ready" if target else "Waiting")

plan_tab, evidence_tab, notes_tab = st.tabs(["Investigation plan", "Evidence", "Notes"])

with plan_tab:
    st.subheader("REA agent workflow")
    steps = [
        ("1. Reconnaissance", "Record the target, environment, entry points, and observable behavior."),
        ("2. Capture", "Collect screenshots, request/response traces, logs, strings, or binaries."),
        ("3. Hypothesize", "Describe the smallest explanation that fits the evidence."),
        ("4. Validate", "Design a repeatable test and compare expected versus observed behavior."),
        ("5. Document", "Keep findings, confidence, and follow-up questions together."),
    ]
    for title, description in steps:
        st.markdown(f"**{title}** — {description}")
    if objective:
        st.subheader("Current objective")
        st.write(objective)

with evidence_tab:
    if uploaded:
        data = uploaded.getvalue()
        st.write(f"**{uploaded.name}** · {len(data):,} bytes")
        st.code(sha256_bytes(data), language="text")
        if uploaded.type and uploaded.type.startswith("text/"):
            st.text_area("Text preview", data.decode("utf-8", errors="replace")[:10_000], height=260)
        else:
            st.caption("Binary preview is omitted; the SHA-256 fingerprint identifies this upload.")
    else:
        st.info("Attach an artifact to fingerprint and preview it here.")

with notes_tab:
    notes = st.text_area("Investigation notes", placeholder="Observations, hypotheses, commands, links, and next steps...", height=320)
    if notes:
        st.download_button("Download notes", data=notes, file_name="rea-investigation-notes.md", mime="text/markdown")

st.divider()
st.caption("Starter app generated for the OWEN-REVERSED-ENG repository. Add your preferred REA/LLM backend behind this interface when ready.")
