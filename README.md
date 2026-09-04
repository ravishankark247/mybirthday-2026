# Ravi Shankar Kumar Birthday Wall

A Streamlit birthday wish wall for Ravi Shankar Kumar. Visitors can publish a name, location, message, and optional photo, video, or audio attachment. Wishes are shown newest first with an ISO timestamp converted to the visitor's local display timezone.

The birthday date is **11 October 2026**. Add the supplied images to these paths for the birthday portrait and gift QR code to appear:

```text
assets/ravi-shankar-kumar.jpg
assets/gift-qr.png
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL printed by Streamlit.

To open the portrait and gift-payment dashboard instead:

```bash
python -m streamlit run dashboard.py
```

## Deploy on Streamlit Community Cloud

1. Push this folder to a GitHub repository.
2. In Streamlit Community Cloud, choose **Create app** and select the repository.
3. Set the main file path to `app.py`.
4. Deploy.

The app uses `st.session_state`, so wishes and uploaded media are intentionally session-based. For permanent shared storage, replace the session state list with a database or object-storage integration.
