import sqlite3

def cadastrarCliente(cpf: str, nome: str, estado: str):
  connection = sqlite3.connect('banco.db')
  cursor = connection.cursor()
  cursor.execute(f"insert into Clientes (cpf, nomeCliente, estado) values ('{cpf}', '{nome}', '{estado}')")
  connection.commit()
  cursor.close()
  connection.close()

def consultarClientes():
  connection = sqlite3.connect('banco.db')
  cursor = connection.cursor()
  cursor.execute('select * from Clientes')
  todosClientes = cursor.fetchall()
  cursor.close()
  connection.close()
  return todosClientes

def atualizarCliente(cpf: str, nome: str, estado: str):
  connection = sqlite3.connect('banco.db')
  cursor = connection.cursor()
  cursor.execute(f"update Clientes set nomeCliente = '{nome}', estado = '{estado}' where cpf = '{cpf}'")
  connection.commit()
  cursor.close()
  connection.close()

def excluirCliente(cpf: str):
  connection = sqlite3.connect('banco.db')
  cursor = connection.cursor()
  cursor.execute(f"delete from Clientes where cpf = '{cpf}'")
  connection.commit()
  cursor.close()
  connection.close()
