import streamlit as st
from database.init_db import criar_banco
criar_banco()
st.set_page_config(page_title="SalonPro MVP",layout="wide")
st.title("💇 SalonPro MVP")
st.write("Use o menu lateral para acessar Clientes, Profissionais, Serviços e Agendamentos.")
