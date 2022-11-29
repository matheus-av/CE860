import numpy as np
import sqlite3
def validaCpf(cpf):
    listaDigitos = [int(digito) for digito in str(cpf) if digito.isdigit()]
    #Checando tamanho correto
    if len(listaDigitos)!= 11:
        print("Erro: CPF Inválido.")
        return False
    somaProdutos = sum(a*b for a, b in zip(listaDigitos[0:9], range(10, 1, -1)))
    digitoCorreto = (somaProdutos * 10 % 11) % 10
    if listaDigitos[9] != digitoCorreto:
        print("Erro: CPF Inválido.")
        return False

    # Validação do segundo dígito verificador:
    somaProdutos = sum(a*b for a, b in zip(listaDigitos[0:10], range(11, 1, -1)))
    digitoCorreto = (somaProdutos * 10 % 11) % 10
    if listaDigitos[10] != digitoCorreto:
        print("Erro: CPF Inválido.")
        return False

def validaNulo(entrada):
    #Checar se o valor é nulo
    if entrada not in ["",np.nan,None]:
        return True
    else:
        print("Erro: Dado Nulo.")
        return False

def checkChaves(campo,tabela,valor):
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
        return False
    else:
        #Não Existe o campo no banco
        return True

def checkQuantidades(quantidades):
    #Validar entrada de quantidades
    if quantidades=="":
        print("Erro: Quantidades nulas.")
        return False
    listaQtds=quantidades.split(',')
    for q in listaQtds:
        if q =="":
            print("Erro: Uma das Quantidades está nula.")
            return False
        if int(q)<=0:
            print("Erro: Uma das quantidades está negativa ou igual a zero.")
            return False
    return True

def skusValidos(skus):
    # Validar entrada de quantidades
    if skus == "":
        print("Erro: SKUs nulas.")
        return False
    listaSkus = skus.split(',')
    for sku in listaSkus:
        if sku == "":
            print("Erro: Uma das SKUs está nula.")
            return False
        if checkChaves('sku','Produtos',sku):
            print('Erro: SKU não existente')
            return False
    return True
