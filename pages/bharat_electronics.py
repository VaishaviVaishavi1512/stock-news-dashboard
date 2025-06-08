import streamlit as st

st.title("Bharat Electronics Stock Page")
st.write("This is Bharat Electronics stock info page.")

if st.button("⬅️ Go back Home"):
    st.experimental_set_query_params()
    st.experimental_rerun()
