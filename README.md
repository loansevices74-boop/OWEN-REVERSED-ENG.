# OWEN REVERSED ENG

A starter Streamlit workspace for reverse-engineering investigations inspired by the `rea-agents` setup.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Open [share.streamlit.io](https://share.streamlit.io/).
2. Select `loansevices74-boop/OWEN-REVERSED-ENG.`.
3. Select branch `feature/streamlit-rea-app`.
4. Set the main file to `app.py`.
5. Deploy.

The app provides a structured investigation workspace, evidence fingerprinting, text previews, and downloadable notes. Add API credentials through Streamlit Secrets before connecting an LLM or external analysis backend.
