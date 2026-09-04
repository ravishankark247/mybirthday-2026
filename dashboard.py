from pathlib import Path
from urllib.parse import quote

import streamlit as st


st.set_page_config(
    page_title="Ravi's birthday dashboard",
    page_icon="🎁",
    layout="centered",
)

ASSET_DIR = Path(__file__).parent / "assets"
PORTRAIT_PATH = ASSET_DIR / "ravi-shankar-kumar.jpg"
QR_PATH = ASSET_DIR / "gift-qr.png"
UPI_ID = "918285326045@waicici"
UPI_PAYMENT_LINK = (
    f"upi://pay?pa={quote(UPI_ID)}&pn={quote('Ravishankar Kumar')}"
    f"&cu=INR&tn={quote('Birthday gift for Ravi Shankar Kumar')}"
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;600;700;800&display=swap');
    :root { --ink: #17232b; --muted: #66747a; --paper: #f7f4ed; --cream: #fffdf8; --coral: #ee765e; --mint: #b9d9c9; --line: #d9ddd5; --blue: #365b68; }
    .stApp { background: var(--paper); color: var(--ink); font-family: 'Manrope', sans-serif; }
    [data-testid='stHeader'] { background: transparent; }
    .block-container { max-width: 760px; padding: 2.5rem 1.25rem 4rem; }
    .eyebrow, .mono { font-family: 'DM Mono', monospace; text-transform: uppercase; letter-spacing: .08em; }
    .eyebrow { color: #c95745; font-size: .7rem; margin-bottom: 1rem; }
    h1 { font-size: clamp(2.6rem, 8vw, 5.8rem) !important; line-height: .95 !important; letter-spacing: -.075em !important; margin: 0 !important; }
    .intro { color: var(--muted); font-size: 1rem; line-height: 1.65; margin: 1.3rem 0 2rem; max-width: 560px; }
    .preview-frame { background: var(--cream); border: 1px solid var(--line); padding: .55rem; transform: rotate(-1deg); margin-bottom: 2.2rem; }
    .preview-frame img { display: block; width: 100%; max-height: 620px; object-fit: cover; object-position: center 35%; }
    .section { border-top: 1px solid var(--line); padding-top: 1.5rem; margin-top: 2.5rem; }
    .section-label { color: #c95745; font: 500 .7rem 'DM Mono', monospace; letter-spacing: .08em; text-transform: uppercase; }
    .section h2 { font-size: 1.9rem; letter-spacing: -.05em; margin: .45rem 0 .5rem; }
    .section p { color: var(--muted); line-height: 1.65; }
    .identity { display: grid; grid-template-columns: repeat(2, 1fr); gap: .75rem; margin-top: 1.1rem; }
    .identity div { background: var(--cream); border: 1px solid var(--line); padding: .9rem 1rem; }
    .identity strong { display: block; font-size: 1.05rem; }
    .identity span { color: var(--muted); font: .62rem 'DM Mono', monospace; letter-spacing: .08em; text-transform: uppercase; }
    .payment { background: var(--blue); color: #fffdf8; padding: 1.5rem; margin-top: 1.2rem; }
    .payment h3 { color: #fffdf8; font-size: 1.35rem; margin: 0 0 .35rem; }
    .payment p { color: #dce8e1; margin: 0 0 1rem; }
    .qr-wrap { background: white; padding: .6rem; margin: 1rem auto 1.25rem; max-width: 360px; }
    .qr-wrap img { display: block; width: 100%; }
    .upi-id { background: rgba(255,255,255,.1); padding: .75rem; font: .8rem 'DM Mono', monospace; word-break: break-all; }
    .stLinkButton a { background: var(--coral); border: 0; border-radius: 0; color: white !important; font-weight: 800; }
    .note { color: #f8d27e; font: .68rem 'DM Mono', monospace; letter-spacing: .05em; text-transform: uppercase; margin-top: 1rem; }
    @media (max-width: 520px) { .identity { grid-template-columns: 1fr; } .payment { padding: 1.1rem; } }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="eyebrow">Ravi Shankar Kumar · birthday dashboard</div>', unsafe_allow_html=True)
st.title("A little celebration, ready to share.")
st.markdown(
    '<p class="intro">Preview Ravi\'s birthday page here, then use the payment scanner below to send a gift directly to his UPI account.</p>',
    unsafe_allow_html=True,
)

if PORTRAIT_PATH.exists():
    st.markdown('<div class="preview-frame">', unsafe_allow_html=True)
    st.image(str(PORTRAIT_PATH), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.error("The portrait asset is missing from assets/ravi-shankar-kumar.jpg.")

st.markdown(
    '<section class="section"><div class="section-label">The guest of honour</div>'
    '<h2>Happy birthday, Ravi.</h2>'
    '<p>Sunday, 11 October 2026 is the big day. Bring your stories, your appetite, and your most questionable dance moves.</p>'
    '<div class="identity"><div><span>Name</span><strong>Ravi Shankar Kumar</strong></div>'
    '<div><span>Occasion</span><strong>11 October 2026</strong></div></div></section>',
    unsafe_allow_html=True,
)

st.markdown(
    '<section class="section"><div class="section-label">Send a birthday gift</div>'
    '<h2>Scan to pay</h2><p>Open any UPI app, scan the code, and enter the amount you would like to send.</p>'
    '<div class="payment"><h3>Gift payment scanner</h3><p>Payments go directly to Ravi Shankar Kumar.</p>',
    unsafe_allow_html=True,
)
if QR_PATH.exists():
    st.markdown('<div class="qr-wrap">', unsafe_allow_html=True)
    st.image(str(QR_PATH), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.warning("The payment QR asset is missing from assets/gift-qr.png.")
st.markdown(f'<div class="upi-id">UPI ID · {UPI_ID}</div>', unsafe_allow_html=True)
st.link_button("Open payment app", UPI_PAYMENT_LINK, use_container_width=True)
st.markdown('<div class="note">No pressure · good wishes are already priceless</div></div></section>', unsafe_allow_html=True)

st.page_link("app.py", label="Open the birthday wish wall →")