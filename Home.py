import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Stock AI Bot - Home", layout="wide")

# --- Title ---
st.title("📈 Stock AI News & Sentiment Bot")
st.markdown("Welcome! Click on a stock below to view its news, sentiment analysis, and price charts.")

# --- Stock List ---
stocks = [
    {"name": "Indigo Airlines", "file": "indigo_airlines"},
    {"name": "SBI", "file": "sbi"},
    {"name": "IRCTC", "file": "irctc"},
    {"name": "TATA Motors", "file": "tata_motors"},
    {"name": "Bharat Electronics", "file": "bharat_electronics"},
]

# --- Layout in cards (3 columns) ---
cols = st.columns(3)
for i, stock in enumerate(stocks):
    with cols[i % 3]:
        st.subheader(f"📌 {stock['name']}")
        st.markdown("Get real-time news, AI sentiment analysis, and price predictions.")
        st.page_link(f"/pages/{stock['file']}.py", label=f"👉 Go to {stock['name']}", icon="📊")

# Optional Footer
st.markdown("---")
st.markdown(
    f"<small>Last updated: {datetime.now().strftime('%B %d, %Y %H:%M')} | Built with ❤️ using Streamlit</small>",
    unsafe_allow_html=True,
)

