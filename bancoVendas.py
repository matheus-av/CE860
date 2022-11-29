import sqlite3
from datetime import date
def cadastrarVenda(codVenda: int,cpfCliente: int,data:date,skus : str, quantidades: str):
    listaQuantidades=quantidades.split(',')
    listaSkus = skus.split(',')
    listaQuantidades=[int(q) for q in listaQuantidades]
    listaSkus = [int(s) for s in listaSkus]

    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    firstSqlString=f"""INSERT INTO Vendas (codVenda,cpfCliente,data)
    values
    ({codVenda},{cpfCliente},{data})
    """
    cursor.execute(firstSqlString)
    connection.commit()
    for sku,qtd in zip(listaSkus,listaQuantidades):
        secondSqlString = f"""INSERT INTO Vendas_Produtos (codVenda,skuProduto,quantidade)
            values
            ({codVenda},{sku},{qtd})
            """
        cursor.execute(secondSqlString)
        connection.commit()
    cursor.close()
    connection.close()

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
    INNER JOIN Clientes c
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
    Clientes c
    ON c.cpf=v.cpfCliente
    WHERE v.codVenda={codVenda}
    GROUP BY v.codVenda,c.nomeCliente
    """)
    dadosGerais = cursor.fetchall()
    cursor.execute(f"""
  SELECT vp.skuProduto,vp.quantidade,p.precoProduto,vp.quantidade*p.precoProduto as valor_total FROM Vendas_Produtos vp
  INNER JOIN Produtos p
  ON p.sku=vp.skuProduto
  WHERE vp.codVenda={codVenda}
    """)
    dadosProdutos = cursor.fetchall()
    cursor.close()
    connection.close()
    return dadosGerais,dadosProdutos

def atualizarVenda(codVenda: int,cpfCliente: int,data:date,skus : str, quantidades: str):
    listaQuantidades = quantidades.split(',')
    listaSkus = skus.split(',')
    listaQuantidades = [int(q) for q in listaQuantidades]
    listaSkus = [int(s) for s in listaSkus]

    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    firstSqlString = f"""UPDATE Vendas SET cpfCliente ={cpfCliente},
    data={data} 
    WHERE
    codVenda={codVenda}
        """
    cursor.execute(firstSqlString)
    connection.commit()
    deleteSqlString = f"""DELETE FROM Vendas_Produtos
    WHERE
    codVenda={codVenda}
        """
    cursor.execute(deleteSqlString)
    connection.commit()
    for sku, qtd in zip(listaSkus, listaQuantidades):
        secondSqlString = f"""INSERT INTO Vendas_Produtos (codVenda,skuProduto,quantidade)
            values
            ({codVenda},{sku},{qtd})
            """
        cursor.execute(secondSqlString)
        connection.commit()
    cursor.close()
    connection.close()

def excluirVenda(codVenda: int):
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    firstSqlString = f"""DELETE FROM Vendas
    WHERE
    codVenda={codVenda}
        """
    cursor.execute(firstSqlString)
    connection.commit()
    secondSqlString = f"""DELETE FROM Vendas_Produtos
    WHERE
    codVenda={codVenda}
        """
    cursor.execute(secondSqlString)
    connection.commit()
excluirVenda(1)
