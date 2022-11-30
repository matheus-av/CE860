import pandas as pd
import sqlite3
from datetime import date

def getRelatorioFromStringSQL(consSqlString):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    connection = sqlite3.connect('banco.db')
    df = pd.read_sql_query(consSqlString, connection)
    return df

def getReceitaTotal(dataInicial,dataFinal):
    consSqlString = f"""SELECT strftime('%Y',v.data) as Ano,strftime('%m',v.data) as Mês, sum(vp.quantidade*p.precoProduto) as Receita_Total FROM Vendas_Produtos vp
    INNER JOIN Produtos p
    ON p.sku=vp.skuProduto
    INNER JOIN Vendas v
    ON v.codVenda=vp.codVenda
    WHERE strftime('%Y-%m-%d',v.data) BETWEEN '{dataInicial}' AND '{dataFinal}'
    GROUP BY Ano,Mês
    """
    df=getRelatorioFromStringSQL(consSqlString)
    if not df.empty:
        return df.to_string(index=False)
    else:
        return "Sem dados para as datas selecionadas."

def getLucrosCustosTotais(dataInicial,dataFinal):
    consSqlString = f"""SELECT strftime('%Y',v.data) as Ano,strftime('%m',v.data) as Mês, sum(vp.quantidade*p.custoProduto) as Custo_Total,
    sum(vp.quantidade*(p.precoProduto-p.custoProduto)) as Custo_Total
    FROM Vendas_Produtos vp
    INNER JOIN Produtos p
    ON p.sku=vp.skuProduto
    INNER JOIN Vendas v
    ON v.codVenda=vp.codVenda
    WHERE strftime('%Y-%m-%d',v.data) BETWEEN '{dataInicial}' AND '{dataFinal}'
    GROUP BY Ano,Mês
    """
    df=getRelatorioFromStringSQL(consSqlString)
    if not df.empty:
        return df.to_string(index=False)
    else:
        return "Sem dados para as datas selecionadas."

def produtosMaisVendidos(dataInicial,dataFinal):
    consSqlString=f"""
    SELECT p.nomeProduto as Produto,p.sku as SKU, p.precoProduto as Preço,sum(vp.quantidade) as Quantidade_Vendida FROM Vendas_Produtos vp
    INNER JOIN Produtos p
    ON p.sku=vp.skuProduto
    INNER JOIN Vendas v
    ON vp.codVenda=v.codVenda
    WHERE strftime('%Y-%m-%d',v.data) BETWEEN '{dataInicial}' AND '{dataFinal}'
    GROUP BY p.nomeProduto
    ORDER BY Quantidade_Vendida DESC
    LIMIT 5
    """
    df=getRelatorioFromStringSQL(consSqlString)
    if not df.empty:
        return df.to_string(index=False)
    else:
        return "Sem dados para as datas selecionadas."

def vendasPorLocalidade(dataInicial,dataFinal):
    consSqlString=f"""
    SELECT c.estado as Estado,count(*) as Número_Pedidos FROM Vendas v
    INNER JOIN Clientes c
    ON c.cpf=v.cpfCliente
    WHERE strftime('%Y-%m-%d',v.data) BETWEEN '{dataInicial}' AND '{dataFinal}'
    GROUP BY c.estado
    """
    df=getRelatorioFromStringSQL(consSqlString)
    if not df.empty:
        return df.to_string(index=False)
    else:
        return "Sem dados para as datas selecionadas."

def clientesMaisAtivos(dataInicial,dataFinal):
    consSqlString=f"""
    SELECT c.nomeCliente as Cliente,c.estado as Estado, count(*) as Número_de_Pedidos FROM Vendas v
    INNER JOIN Clientes c
    ON v.cpfCliente=c.cpf
    WHERE strftime('%Y-%m-%d',v.data) BETWEEN '{dataInicial}' AND '{dataFinal}'
    GROUP BY c.nomeCliente
    ORDER BY Número_de_Pedidos DESC
    LIMIT 5
    """
    df=getRelatorioFromStringSQL(consSqlString)
    if not df.empty:
        return df.to_string(index=False)
    else:
        return "Sem dados para as datas selecionadas."
