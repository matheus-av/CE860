import numpy as np
import sqlite3

def existeChavePrimaria(campo, tabela, valor):
    # Função para checar a existência de uma chave primária no banco
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    stringConsulta=f'select * from {tabela} WHERE {campo}={valor}'
    cursor.execute(stringConsulta)
    resultado = cursor.fetchall()
    cursor.close()
    connection.close()
    if resultado !=[]:
        #Existe o campo no banco
        return True
    else:
        #Não Existe o campo no banco
        return False

def cpfValido(cpf):
    listaDigitos = [int(digito) for digito in str(cpf) if digito.isdigit()]
    #Checando tamanho correto
    if len(listaDigitos)!= 11:
        return False
    somaProdutos = sum(a*b for a, b in zip(listaDigitos[0:9], range(10, 1, -1)))
    digitoCorreto = (somaProdutos * 10 % 11) % 10
    if listaDigitos[9] != digitoCorreto:
        return False

    # Validação do segundo dígito verificador:
    somaProdutos = sum(a*b for a, b in zip(listaDigitos[0:10], range(11, 1, -1)))
    digitoCorreto = (somaProdutos * 10 % 11) % 10
    if listaDigitos[10] != digitoCorreto:
        return False

    if existeChavePrimaria('cpf', 'Clientes', cpf):
        return False
    else:
        return True

def ehNulo(entrada):
    #Checar se o valor é nulo
    if entrada not in ["",np.nan,None]:
        return True
    else:
        return False
    
def estadoValido(estado):
    lista = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO",
             "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR",
             "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]
    if estado in lista:
        return True
    else:
        return False
    
def quantidadesValidas(quantidades):
    #Validar entrada de quantidades
    if quantidades=="":
        return False
    listaQtds=quantidades.split(',')
    for q in listaQtds:
        if q =="":
            return False
        if int(q)<=0:
            return False
    return True

def skusValidos(skus):
    # Validar entrada de quantidades
    if skus == "":
        return False
    listaSkus = skus.split(',')
    for sku in listaSkus:
        if sku == "":
            return False
        if existeChavePrimaria('sku','Produtos',sku):
            return False
    return True
