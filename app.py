from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote

import streamlit as st


st.set_page_config(
    page_title="A note for Ravi Shankar Kumar",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)


CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --ink: #17232b;
    --muted: #66747a;
    --paper: #f7f4ed;
    --cream: #fffdf8;
    --coral: #ee765e;
    --coral-dark: #c95745;
    --mint: #b9d9c9;
    --line: #d9ddd5;
    --blue: #365b68;
}

.stApp {
    background: var(--paper);
    color: var(--ink);
    font-family: 'Manrope', sans-serif;
}

[data-testid="stHeader"] { background: transparent; }
.block-container { max-width: 1180px; padding: 3rem 3rem 5rem; }

.eyebrow, .mono, .stamp, .stat-label {
    font-family: 'DM Mono', monospace;
    text-transform: uppercase;
    letter-spacing: .08em;
}

.eyebrow { color: var(--coral-dark); font-size: .7rem; font-weight: 500; margin-bottom: 1.2rem; }
.hero { position: relative; padding: 1.4rem 0 2.8rem; border-bottom: 1px solid var(--line); overflow: hidden; }
.hero:before { content: ''; position: absolute; width: 420px; height: 420px; right: 10%; top: -180px; border: 1px solid rgba(238,118,94,.24); border-radius: 50%; box-shadow: 0 0 0 34px rgba(238,118,94,.05), 0 0 0 70px rgba(238,118,94,.035); animation: orbit 14s linear infinite; }
.hero:after { content: '✦'; position: absolute; right: 5%; top: -1.4rem; color: var(--coral); font-size: 14rem; line-height: 1; opacity: .16; transform: rotate(16deg); }
.hero h1 { max-width: 820px; margin: 0; color: var(--ink); font-size: clamp(3.4rem, 8vw, 7.2rem); line-height: .92; letter-spacing: -.075em; font-weight: 800; position: relative; z-index: 1; }
.hero h1 span { color: var(--coral); }
.hero-copy { max-width: 560px; margin-top: 1.8rem; color: var(--muted); font-size: 1.05rem; line-height: 1.7; position: relative; z-index: 1; }
.birthday-date { display: inline-block; margin-top: 1.25rem; background: var(--ink); color: #fffdf8; padding: .55rem .8rem; font-family: 'DM Mono', monospace; font-size: .72rem; letter-spacing: .08em; text-transform: uppercase; }
.countdown-shell { background: var(--ink); color: #fffdf8; padding: 1rem 1.2rem; margin: 1.3rem 0 1rem; display: flex; align-items: center; justify-content: space-between; gap: 1rem; }
.countdown-label { color: #b9d9c9; font-family: 'DM Mono', monospace; font-size: .65rem; text-transform: uppercase; letter-spacing: .08em; }
.countdown-value { font-size: 1.2rem; font-weight: 800; letter-spacing: -.03em; }
.portrait-frame { border: 1px solid var(--line); background: var(--cream); padding: .45rem; transform: rotate(2deg); }
.portrait-frame img { display: block; width: 100%; aspect-ratio: 4 / 5; object-fit: cover; }
.asset-placeholder { min-height: 260px; display: grid; place-items: center; text-align: center; color: var(--muted); background: #edf2ec; padding: 2rem; }
.gift-section { background: var(--blue); color: #fffdf8; padding: 1.8rem; margin-top: 3.8rem; }
.gift-section h2 { margin: 0; color: #fffdf8; font-size: 1.8rem; letter-spacing: -.04em; }
.gift-section p { color: #dce8e1; line-height: 1.65; }
.gift-qr { background: white; padding: .5rem; max-width: 300px; }
.gift-note { color: #f8d27e; font-family: 'DM Mono', monospace; font-size: .72rem; text-transform: uppercase; letter-spacing: .06em; }

.stat-row { display: flex; gap: 1rem; margin-top: 2rem; }
.stat { background: var(--cream); border: 1px solid var(--line); padding: .85rem 1.2rem; min-width: 130px; }
.stat-value { font-size: 1.35rem; font-weight: 800; color: var(--blue); }
.stat-label { color: var(--muted); font-size: .63rem; margin-top: .2rem; }

.section-title { display: flex; align-items: baseline; justify-content: space-between; gap: 1rem; margin: 3.8rem 0 1.2rem; }
.section-title h2 { margin: 0; font-size: 1.8rem; letter-spacing: -.04em; }
.section-title p { color: var(--muted); margin: 0; font-size: .9rem; }

.form-shell { background: var(--cream); border: 1px solid var(--line); border-top: 5px solid var(--coral); padding: 1.6rem 1.6rem .7rem; }
.form-shell h3 { margin: 0 0 .3rem; font-size: 1.35rem; }
.form-shell .helper { color: var(--muted); font-size: .84rem; margin-bottom: 1.2rem; }
label, [data-testid="stWidgetLabel"] p { color: var(--ink) !important; font-size: .8rem !important; font-weight: 700 !important; }
input, textarea, [data-baseweb="select"] > div { background: #fffefb !important; border-color: var(--line) !important; border-radius: 0 !important; }
.stButton > button { background: var(--coral); color: white; border: 0; border-radius: 0; font-weight: 800; padding: .7rem 1.4rem; transition: transform .2s ease, background .2s ease; }
.stButton > button:hover { background: var(--coral-dark); transform: translateY(-2px); }
[data-testid="stFileUploader"] { border: 1px dashed #b6c3bb; border-radius: 0; background: #f5f7f1; }

.feed-intro { border-bottom: 1px solid var(--line); padding-bottom: .8rem; color: var(--muted); font-size: .9rem; }
.wish { background: var(--cream); border: 1px solid var(--line); border-left: 5px solid var(--mint); padding: 1.35rem 1.5rem; margin: 1rem 0; animation: rise .45s ease both; }
.wish:nth-of-type(odd) { border-left-color: var(--coral); }
.wish-head { display: flex; justify-content: space-between; gap: 1rem; align-items: start; }
.wish-name { font-size: 1.15rem; font-weight: 800; }
.wish-message { margin: .8rem 0 1rem; font-size: 1rem; line-height: 1.65; color: #34444a; white-space: pre-wrap; }
.stamp { color: var(--muted); font-size: .62rem; line-height: 1.7; text-align: right; white-space: nowrap; }
.media-tag { display: inline-block; background: var(--mint); color: #23453e; padding: .25rem .5rem; font-size: .7rem; font-weight: 800; margin-bottom: .8rem; }
.wish-vibe { color: var(--coral-dark); font-family: 'DM Mono', monospace; font-size: .65rem; letter-spacing: .06em; text-transform: uppercase; margin-top: .45rem; }
.empty { background: #eef3ec; border: 1px solid #d4e1d6; padding: 2rem; color: var(--muted); }
.footer { border-top: 1px solid var(--line); margin-top: 4rem; padding-top: 1rem; color: var(--muted); font-size: .75rem; }
@keyframes rise { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
@keyframes orbit { to { transform: rotate(360deg); } }
@media (max-width: 700px) { .block-container { padding: 2rem 1.1rem 3rem; } .hero h1 { font-size: 3.7rem; } .hero:after { right: -5%; font-size: 9rem; } .hero:before { right: -45%; } .stat-row { flex-wrap: wrap; } .stat { flex: 1; min-width: 100px; } .wish-head { display: block; } .stamp { text-align: left; margin-top: .5rem; } .countdown-shell { display: block; } }
</style>
"""


DEFAULT_WISHES: list[dict[str, Any]] = [
    {
        "name": "The people who root for you",
        "location": "Everywhere",
        "message": "May this year bring you brave ideas, quiet wins, and plenty of reasons to celebrate. Happy birthday, Ravi!",
        "created_at": "2026-01-01T09:30:00+00:00",
        "vibe": "Warm & wonderful",
        "media": None,
    },
]

ASSET_DIR = Path(__file__).parent / "assets"
PORTRAIT_PATH = ASSET_DIR / "ravi-shankar-kumar.jpg"
QR_PATH = ASSET_DIR / "gift-qr.png"
UPI_ID = "918285326045@waicici"
UPI_PAYMENT_LINK = (
    f"upi://pay?pa={quote(UPI_ID)}&pn={quote('Ravishankar Kumar')}&cu=INR"
    f"&tn={quote('Birthday gift for Ravi Shankar Kumar')}"
)


if "wishes" not in st.session_state:
    st.session_state.wishes = DEFAULT_WISHES.copy()

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.markdown(
    """
    <header class="hero">
        <div class="eyebrow">A little corner of the internet · 2026</div>
        <h1>Happy birthday,<br><span>Ravi Shankar Kumar.</span></h1>
        <p class="hero-copy">A living wall of good wishes from the people who are glad you are here. Leave a note, add a memory, and make this day a little louder.</p>
        <div class="birthday-date">11 October 2026 · The big day</div>
    </header>
    """,
    unsafe_allow_html=True,
)

portrait_col, intro_col = st.columns([1, 2], gap="large")
with portrait_col:
    if PORTRAIT_PATH.exists():
        st.markdown('<div class="portrait-frame">', unsafe_allow_html=True)
        st.image(str(PORTRAIT_PATH), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="asset-placeholder">Add the provided portrait as<br><strong>assets/ravi-shankar-kumar.jpg</strong></div>', unsafe_allow_html=True)
with intro_col:
    st.markdown('<div class="section-title"><h2>Save the date</h2></div>', unsafe_allow_html=True)
    st.markdown('<p class="hero-copy">The celebration lands on <strong>Sunday, 11 October 2026</strong>. Bring your stories, your appetite, and your most questionable dance moves.</p>', unsafe_allow_html=True)

countdown_target = datetime(2026, 10, 11, tzinfo=timezone.utc)
countdown_delta = countdown_target - datetime.now(timezone.utc)
if countdown_delta.total_seconds() > 0:
        countdown_days = countdown_delta.days
        countdown_hours, remainder = divmod(countdown_delta.seconds, 3600)
        countdown_minutes, countdown_seconds = divmod(remainder, 60)
        countdown_text = f"{countdown_days}d {countdown_hours}h {countdown_minutes}m {countdown_seconds}s"
else:
        countdown_text = "It is Ravi's birthday! 🎉"
st.markdown(
        f'<div class="countdown-shell"><div><div class="countdown-label">Countdown to the big day</div><div class="countdown-value">{countdown_text}</div></div><div aria-hidden="true">🎈 ✦ 🎂</div></div>',
        unsafe_allow_html=True,
)

wish_count = len(st.session_state.wishes)
media_count = sum(1 for wish in st.session_state.wishes if wish.get("media"))
col_a, col_b, col_c = st.columns([1, 1, 2])
with col_a:
    st.markdown(f'<div class="stat"><div class="stat-value">{wish_count:02d}</div><div class="stat-label">Wishes collected</div></div>', unsafe_allow_html=True)
with col_b:
    st.markdown(f'<div class="stat"><div class="stat-value">{media_count:02d}</div><div class="stat-label">Memories attached</div></div>', unsafe_allow_html=True)
with col_c:
    st.markdown('<div class="stat"><div class="stat-value">Today + always</div><div class="stat-label">The occasion</div></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title"><h2>Leave your mark</h2><p>Tell Ravi where the good wishes are coming from.</p></div>', unsafe_allow_html=True)

with st.container(border=False):
    st.markdown('<div class="form-shell"><h3>Write a birthday wish</h3><div class="helper">Your note will appear in the celebration feed below.</div></div>', unsafe_allow_html=True)
    with st.form("birthday_wish_form", clear_on_submit=True):
        name_col, location_col = st.columns(2)
        with name_col:
            name = st.text_input("Your name", placeholder="e.g. Priya Menon")
        with location_col:
            location = st.text_input("Your location", placeholder="e.g. Bengaluru, India")
        message = st.text_area("Your message", placeholder="Write something Ravi will want to read twice...", height=125)
        vibe = st.selectbox("What is the energy?", ["Warm & wonderful", "Loud & legendary", "Funny & chaotic", "Calm & heartfelt"])
        media = st.file_uploader(
            "Attach a photo, video, or audio memory (optional)",
            type=["jpg", "jpeg", "png", "webp", "mp4", "mov", "mp3", "wav", "m4a"],
            accept_multiple_files=False,
        )
        submitted = st.form_submit_button("Publish birthday wish", use_container_width=False)

    if submitted:
        if not name.strip() or not location.strip() or not message.strip():
            st.error("Please add your name, location, and a message before publishing.")
        else:
            media_record = None
            if media is not None:
                media_record = {"name": media.name, "type": media.type, "bytes": media.getvalue()}
            st.session_state.wishes.insert(
                0,
                {
                    "name": name.strip(),
                    "location": location.strip(),
                    "message": message.strip(),
                    "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    "vibe": vibe,
                    "media": media_record,
                },
            )
            st.success("Your birthday wish is live below.")

            st.session_state.just_published = True
            st.rerun()

if st.session_state.pop("just_published", False):
    st.balloons()

wish_count = len(st.session_state.wishes)
media_count = sum(1 for wish in st.session_state.wishes if wish.get("media"))
st.markdown('<div class="section-title"><h2>The birthday feed</h2><p>Newest notes appear first.</p></div>', unsafe_allow_html=True)
st.markdown(f'<div class="feed-intro">{wish_count} note{"s" if wish_count != 1 else ""} in Ravi\'s celebration archive</div>', unsafe_allow_html=True)

for wish in st.session_state.wishes:
    created_at = datetime.fromisoformat(wish["created_at"])
    readable_time = created_at.astimezone().strftime("%d %b %Y · %H:%M %Z")
    media_record = wish.get("media")
    st.markdown('<article class="wish">', unsafe_allow_html=True)
    if media_record:
        st.markdown(f'<div class="media-tag">ATTACHED · {media_record["name"]}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="wish-head"><div class="wish-name">{wish["name"]}</div><div class="stamp">{readable_time}<br>{wish["location"]}</div></div>'
        f'<div class="wish-message">{wish["message"]}</div><div class="wish-vibe">Mood · {wish.get("vibe", "Warm & wonderful")}</div>',
        unsafe_allow_html=True,
    )
    if media_record:
        media_type = media_record["type"]
        if media_type.startswith("image/"):
            st.image(media_record["bytes"], use_container_width=True)
        elif media_type.startswith("video/"):
            st.video(media_record["bytes"])
        elif media_type.startswith("audio/"):
            st.audio(media_record["bytes"])
    st.markdown('</article>', unsafe_allow_html=True)

st.markdown(
    '<section class="gift-section"><div class="section-title"><h2>Gift Ravi a little joy 🎁</h2></div>'
    '<p>Want to send a birthday gift? Scan the UPI code with your payment app and let the celebration budget begin. 📱💸🎂</p>'
    '<div class="gift-note">No pressure. Good wishes are already priceless. ✨</div></section>',
    unsafe_allow_html=True,
)
if QR_PATH.exists():
    payment_col, qr_col = st.columns([1, 1], gap="large")
    with payment_col:
        st.markdown("### Send a gift digitally 📲")
        st.markdown(f"UPI ID: `{UPI_ID}`")
        st.link_button("Pay with a UPI app 💸", UPI_PAYMENT_LINK, use_container_width=True)
        st.caption("Works with compatible UPI apps on your phone. Amount is entered in the payment app.")
    with qr_col:
        st.image(str(QR_PATH), caption="Scan to send a birthday gift · Ravi Shankar Kumar", width=300)
else:
    st.markdown("### Send a gift digitally 📲")
    st.markdown(f"UPI ID: `{UPI_ID}`")
    st.link_button("Pay with a UPI app 💸", UPI_PAYMENT_LINK, use_container_width=False)
    st.info("Add the provided payment QR image as assets/gift-qr.png to show it here.")

st.markdown('<div class="footer">Made for Ravi Shankar Kumar · Wishes live in this browser session and reset when the app restarts.</div>', unsafe_allow_html=True)
