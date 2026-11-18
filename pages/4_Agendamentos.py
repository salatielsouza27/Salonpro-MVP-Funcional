import streamlit as st
import pandas as pd
from database.connection import conectar

conn = conectar()

st.title("📅 Agendamentos")

clientes = pd.read_sql(
    "SELECT nome FROM clientes",
    conn
)

profissionais = pd.read_sql(
    "SELECT nome FROM profissionais",
    conn
)

servicos = pd.read_sql(
    "SELECT nome FROM servicos",
    conn
)

if len(clientes) == 0 or len(profissionais) == 0 or len(servicos) == 0:

    st.warning(
        "Cadastre clientes, profissionais e serviços primeiro"
    )

else:

    cliente = st.selectbox(
        "Cliente",
        clientes["nome"]
    )

    profissional = st.selectbox(
        "Profissional",
        profissionais["nome"]
    )

    servico = st.selectbox(
        "Serviço",
        servicos["nome"]
    )

    data = st.date_input("Data")

    horario = st.selectbox(
        "Horário",
        [
            "08:00",
            "09:00",
            "10:00",
            "11:00",
            "14:00",
            "15:00",
            "16:00",
            "17:00"
        ]
    )

    if st.button("Agendar"):

        horario_ocupado = pd.read_sql(
            """
            SELECT *
            FROM agendamentos
            WHERE data = ?
            AND horario = ?
            AND profissional = ?
            """,
            conn,
            params=[
                str(data),
                horario,
                profissional
            ]
        )

        if len(horario_ocupado) > 0:

            st.error(
                f"{profissional} já possui um agendamento às {horario}"
            )

        else:

            conn.execute(
                """
                INSERT INTO agendamentos
                (
                    cliente,
                    profissional,
                    servico,
                    data,
                    horario
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    cliente,
                    profissional,
                    servico,
                    str(data),
                    horario
                )
            )

            conn.commit()

            st.success(
                "Agendamento realizado com sucesso!"
            )

st.subheader("Agendamentos Cadastrados")

agenda = pd.read_sql(
    """
    SELECT *
    FROM agendamentos
    ORDER BY data, horario
    """,
    conn
)

st.dataframe(
    agenda,
    use_container_width=True
)
