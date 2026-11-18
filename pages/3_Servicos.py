import streamlit as st,pandas as pd
from database.connection import conectar
st.title("Serviços")
conn=conectar()
with st.form("serv"):
 nome=st.text_input("Serviço")
 valor=st.number_input("Valor",0.0)
 duracao=st.number_input("Duração (min)",15)
 if st.form_submit_button("Salvar") and nome:
  conn.execute("INSERT INTO servicos(nome,valor,duracao) VALUES (?,?,?)",(nome,float(valor),int(duracao)))
  conn.commit();st.success("Serviço salvo")
st.dataframe(pd.read_sql("select * from servicos",conn),use_container_width=True)
