import sqlite3
def cadastrarVenda():
    #Vou terminar hoje cedo

def consultarTodasVendas():
  connection = sqlite3.connect('banco.db')
  cursor = connection.cursor()
  cursor.execute("""
  WITH VP AS(
  SELECT vp.codVenda,vp.skuProduto,vp.quantidade,vp.quantidade*p.precoProduto as valor_total FROM Vendas_Produtos vp
  INNER JOIN Produtos p
  ON p.sku=vp.skuProduto
  )
    SELECT v.codVenda,c.nomeCliente,v.data,SUM(vp.valor_total) from Vendas v 
    INNER JOIN
    VP
    ON VP.codVenda=v.codVenda
    INNER Clientes c
    ON c.cpf=v.cpfCliente
    GROUP BY v.codVenda,c.nomeCliente
  """)
  todasVendas = cursor.fetchall()
  cursor.close()
  connection.close()
  return todasVendas

def consultarVenda(codVenda: int):
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    cursor.execute(f"""
    SELECT v.codVenda,c.nomeCliente,v.data from Vendas v INNER JOIN
    INNER Clientes c
    ON c.cpf=v.cpfCliente
    GROUP BY v.codVenda,c.nomeCliente
    WHERE v.codVenda={codVenda}
    """)
    dadosGerais = cursor.fetchall()
    cursor.execute(f"""
  SELECT vp.skuProduto,vp.quantidade,p.precoProduto,vp.quantidade*p.precoProduto as valor_total FROM Vendas_Produtos vp
  INNER JOIN Produtos p
  ON p.sku=vp.skuProduto
  WHERE v.codVenda={codVenda}
    """)
    dadosProdutos = cursor.fetchall()
    cursor.close()
    connection.close()
    return dadosGerais,dadosProdutos

def atualizarCVenda():
    print('teste')
    # Vou terminar hoje cedo

def excluirVenda(codVenda: str):
    print('teste')
    # Vou terminar hoje cedo