import streamlit as st,pandas as pd
from database.connection import conectar
st.title("Profissionais")
conn=conectar()
with st.form("prof"):
 nome=st.text_input("Nome")
 esp=st.text_input("Especialidade")
 if st.form_submit_button("Salvar") and nome:
  conn.execute("INSERT INTO profissionais(nome,especialidade) VALUES (?,?)",(nome,esp))
  conn.commit();st.success("Profissional salvo")
st.dataframe(pd.read_sql("select * from profissionais",conn),use_container_width=True)
