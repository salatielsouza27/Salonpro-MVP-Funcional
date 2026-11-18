import streamlit as st
from database.init_db import criar_banco
criar_banco()
st.set_page_config(page_title="SalonPro",page_icon="💇",layout="wide")
st.title("💇 SalonPro")
st.write("Sistema para salões de beleza")
