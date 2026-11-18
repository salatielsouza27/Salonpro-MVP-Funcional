import streamlit as st,pandas as pd
from database.connection import conectar
st.title("Agenda")
conn=conectar()
st.dataframe(pd.read_sql('select * from agendamentos order by data,horario',conn),use_container_width=True)
