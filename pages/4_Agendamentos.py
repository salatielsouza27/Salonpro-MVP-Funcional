horario_ocupado = pd.read_sql(
    """
    SELECT *
    FROM agendamentos
    WHERE data = ?
      AND horario = ?
      AND profissional = ?
    """,
    conn,
    params=[str(data), horario, profissional]
)

if len(horario_ocupado) > 0:
    st.error(
        f"{profissional} já possui um atendimento às {horario}."
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
        VALUES
        (?, ?, ?, ?, ?)
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

    st.success("Agendamento realizado com sucesso.")
