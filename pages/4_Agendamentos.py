import streamlit as st,pandas as pd
from database.connection import conectar
conn=conectar()
st.title("Agendamentos")
clientes=pd.read_sql('select nome from clientes',conn)
prof=pd.read_sql('select nome from profissionais',conn)
serv=pd.read_sql('select nome from servicos',conn)
if len(clientes)==0 or len(prof)==0 or len(serv)==0:
 st.warning('Cadastre clientes, profissionais e serviços primeiro')
else:
 cliente=st.selectbox('Cliente',clientes['nome'])
 profissional=st.selectbox('Profissional',prof['nome'])
 servico=st.selectbox('Serviço',serv['nome'])
 data=st.date_input('Data')
 horario=st.selectbox('Horário',['08:00','09:00','10:00','11:00','14:00','15:00','16:00'])
 if st.button('Agendar'):
  existe=pd.read_sql(f"select * from agendamentos where data='{data}' and horario='{horario}' and profissional='{profissional}'",conn)
  if len(existe)>0: st.error('Horário ocupado')
  else:
   conn.execute('INSERT INTO agendamentos(cliente,profissional,servico,data,horario) VALUES (?,?,?,?,?)',(cliente,profissional,servico,str(data),horario))
   conn.commit();st.success('Agendado')
