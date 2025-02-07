import streamlit as st
from sunsin_lunch.db import select_table

st.set_page_config(page_title="SELECT", page_icon="🍽️")

st.markdown("# 🍽️ SELECT Menu")
st.sidebar.header("SELECT Menu")

st.subheader("확인")
select_df = select_table()
select_df