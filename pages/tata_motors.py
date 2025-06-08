import streamlit as st

st.title("TATA Motors Stock Page")
st.write("This is TATA Motors stock info page.")

if st.button("⬅️ Go back Home"):
    st.experimental_set_query_params()
    st.experimental_rerun()
