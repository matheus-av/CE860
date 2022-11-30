import sqlite3

def criarTabelaProdutos():
  connection = sqlite3.connect('banco.db')
  cursor = connection.cursor()
  sqlProdutos = '''
    create table Produtos(
      sku integer not null primary key,
      nome text not null,
      preco real not null,
      custo real not null
    )'''
  cursor.execute(sqlProdutos)
  connection.commit()
  cursor.close()
  connection.close()

def cadastrarProduto(sku: int, nome: str, preco: float, custo: float):
  connection = sqlite3.connect('banco.db')
  cursor = connection.cursor()
  cursor.execute(f"insert into Produtos (sku, nomeProduto, precoProduto, custoProduto) values ({sku}, '{nome}', {preco}, {custo})")
  connection.commit()
  cursor.close()
  connection.close()

def consultarProdutos():
  connection = sqlite3.connect('banco.db')
  cursor = connection.cursor()
  cursor.execute('select * from Produtos')
  todosProdutos = cursor.fetchall()
  cursor.close()
  connection.close()
  return todosProdutos

def atualizarProduto(sku: int, nome: str, preco: float, custo: float):
  connection = sqlite3.connect('banco.db')
  cursor = connection.cursor()
  cursor.execute(f"update Produtos set nomeProduto = '{nome}', precoProduto = {preco}, custoProduto = {custo} where sku = {sku}")
  connection.commit()
  cursor.close()
  connection.close()

def excluirProduto(sku: str):
  connection = sqlite3.connect('banco.db')
  cursor = connection.cursor()
  cursor.execute(f"delete from Produtos where sku = {sku}")
  connection.commit()
  cursor.close()
  connection.close()
