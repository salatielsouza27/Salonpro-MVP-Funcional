import streamlit as st,pandas as pd
from database.connection import conectar
st.title("Clientes")
conn=conectar()
with st.form("cliente"):
 nome=st.text_input("Nome")
 telefone=st.text_input("Telefone")
 email=st.text_input("Email")
 if st.form_submit_button("Salvar") and nome:
  conn.execute("INSERT INTO clientes(nome,telefone,email) VALUES (?,?,?)",(nome,telefone,email))
  conn.commit();st.success("Cliente salvo")
st.dataframe(pd.read_sql("select * from clientes",conn),use_container_width=True)
