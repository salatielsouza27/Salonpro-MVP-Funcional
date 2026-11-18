from database.connection import conectar

def criar_banco():
    conn=conectar();c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT,telefone TEXT,email TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS profissionais(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT,especialidade TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS servicos(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT,valor REAL,duracao INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS agendamentos(id INTEGER PRIMARY KEY AUTOINCREMENT,cliente TEXT,profissional TEXT,servico TEXT,data TEXT,horario TEXT)")
    conn.commit();conn.close()
