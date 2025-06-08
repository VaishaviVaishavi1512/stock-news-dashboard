import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Stock AI Bot - Home", layout="wide")

st.title("📈 Stock AI News & Sentiment Bot")
st.markdown("Welcome! Click on a stock below to view its news, sentiment analysis, and price charts.")

# Stock data
stocks = [
    {"name": "Indigo Airlines", "page": "indigo_airlines"},
    {"name": "SBI", "page": "sbi"},
    {"name": "IRCTC", "page": "irctc"},
    {"name": "TATA Motors", "page": "tata_motors"},
    {"name": "Bharat Electronics", "page": "bharat_electronics"},
]

# 3 columns layout
cols = st.columns(3)
for i, stock in enumerate(stocks):
    with cols[i % 3]:
        st.subheader(f"📌 {stock['name']}")
        st.markdown("Real-time news, sentiment analysis, and stock price charts.")
        if st.button(f"Open {stock['name']}", key=stock['page']):
            st.switch_page(f"pages/{stock['page']}.py")

# Footer
st.markdown("---")
st.markdown(
    f"<small>Last updated: {datetime.now().strftime('%B %d, %Y %H:%M')} | Built with ❤️ using Streamlit</small>",
    unsafe_allow_html=True,
)

