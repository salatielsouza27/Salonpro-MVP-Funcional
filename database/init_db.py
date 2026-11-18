from database.connection import conectar
def criar_banco():
 c=conectar();cur=c.cursor()
 cur.execute("CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY,nome TEXT,telefone TEXT,email TEXT)")
 cur.execute("CREATE TABLE IF NOT EXISTS profissionais(id INTEGER PRIMARY KEY,nome TEXT,especialidade TEXT)")
 cur.execute("CREATE TABLE IF NOT EXISTS servicos(id INTEGER PRIMARY KEY,nome TEXT,valor REAL,duracao INTEGER)")
 cur.execute("CREATE TABLE IF NOT EXISTS agendamentos(id INTEGER PRIMARY KEY,cliente TEXT,profissional TEXT,servico TEXT,data TEXT,horario TEXT)")
 c.commit();c.close()
