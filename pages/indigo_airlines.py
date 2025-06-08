import streamlit as st

st.title("Indigo Airlines Stock Page")
st.write("This is Indigo Airlines stock info page.")

if st.button("⬅️ Go back Home"):
    st.experimental_set_query_params()
    st.experimental_rerun()

