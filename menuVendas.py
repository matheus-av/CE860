import validacoes
import bancoVendas
import pandas as pd
from datetime import date
def menuVendas():
    while True:
        print('1 - Cadastrar Venda')
        print('2 - Consultar Vendas')
        print('3 - Atualizar Venda')
        print('4 - Excluir Venda')
        print('0 - Sair')

        opcao = input('Digite o número de uma opção:')

        if opcao == "1":
            cadastrarVenda()
        elif opcao == "2":
            consultarVendas()
        elif opcao == "3":
            atualizarVenda()
        elif opcao == "4":
            excluirVenda()
        elif opcao == "0":
            break
        else:
            print('Opção inválida')

def cadastrarVenda():
    codigo = input('Digite o código da venda:')
    while (not validacoes.codigoValido(codigo)) or (validacoes.existeChavePrimaria('codVenda','Vendas',codigo)):
        if not validacoes.codigoValido(codigo):
            print('Código inválido')
        elif validacoes.existeChavePrimaria('codVenda','Vendas',codigo):
            print('Código existente')
        codigo = input('Digite o código da venda:')
    codigo=int(codigo)
    cpf = input('Digite o CPF do cliente:')
    while (not validacoes.cpfValido(cpf)) or (not validacoes.existeChavePrimaria('cpf','Clientes',cpf)):
        if not validacoes.cpfValido(cpf):
            print('CPF inválido')
        elif not validacoes.existeChavePrimaria('cpf','Clientes',cpf):
            print('CPF inexistente')
        cpf = input('Digite o CPF do cliente:')

    data = input('Digite a DATA da venda (Formato Dia/Mês/Ano):')
    while not validacoes.dataValida(data):
        print('DATA inválida')
        data = input('Digite a DATA da venda (Formato Dia/Mês/Ano):')
    data= date(int(data.split('/')[2]),int(data.split('/')[1]),int(data.split('/')[0]))
    skus=list()
    quantidades=list()
    maisProduto = True
    while maisProduto:
        sku = input('Digite o SKU do produto:')
        while (not validacoes.skuValido(sku)) or (not validacoes.existeChavePrimaria('sku','Produtos',int(sku))):
            if not validacoes.skuValido(sku):
                print('SKU inválido')
            elif not validacoes.existeChavePrimaria('sku','Produtos',sku):
                print('SKU inexistente.')
            sku = input('Digite o SKU do produto:')
        skus.append(int(sku))
        quantidade = input('Digite a QUANTIDADE do produto:')
        while not validacoes.quantidadeValida(quantidade):
            print('QUANTIDADE inválida')
            quantidade = input('Digite a QUANTIDADE do produto:')
        quantidades.append(int(quantidade))
        
        opcao = input('Mais algum produto? (S/N):')
        while opcao.lower() not in ['s', 'n']:
            print('Opção inválida')
            opcao = input('Mais algum produto? (S/N):')

        if opcao.lower() == 's':
            maisProduto = True
        elif opcao.lower() == 'n':
            maisProduto = False
        
    bancoVendas.cadastrarVenda(codigo,cpf,data,skus,quantidades)
    print('Venda Cadastrada')

def consultarVendas():
    resultados=bancoVendas.consultarTodasVendas()
    cods=[r[0] for r in resultados]
    nomes = [r[1] for r in resultados]
    datas = [r[2] for r in resultados]
    valores = [r[3] for r in resultados]
    dfExibir =pd.DataFrame({'Código_da_Venda':cods,
                            'Nome_do_Cliente':nomes,
                            'Data':datas,
                            'Valor_Total':valores
                            })
    print(dfExibir.to_string())

def atualizarVenda():
    codigo = input('Digite o código da venda:')
    while (not validacoes.codigoValido(codigo)) or (not validacoes.existeChavePrimaria('codVenda','Vendas',codigo)):
        if not validacoes.codigoValido(codigo):
            print('Código inválido')
        elif not validacoes.existeChavePrimaria('codVenda','Vendas',codigo):
            print('Código inexistente')
        codigo = input('Digite o código da venda:')
    codigo=int(codigo)
    dadosGerais,dadosProduto=bancoVendas.consultarVenda(codigo)
    print(dadosGerais)
    print("Abaixo os dados da venda selecionada:\n")
    print(f"Código da Venda:{dadosGerais[0][0]}\n")
    print(f"Nome do Cliente:{dadosGerais[0][1]}\n")
    print(f"CPF:{dadosGerais[0][2]}\n")
    print(f"Data:{dadosGerais[0][3]}\n")
    print("Relação de produtos:\n")
    for p in dadosProduto:
        print(f"SKU: {p[0]} Nome: {p[1]} Quantidade: {p[2]} Preço: {p[3]} Valor Total:{p[4]}\n")
    print("Insira abaixo os novos dados:\n")
    cpf = input('Digite o CPF do cliente:')
    while (not validacoes.cpfValido(cpf)) or (not validacoes.existeChavePrimaria('cpf', 'Clientes', cpf)):
        if not validacoes.cpfValido(cpf):
            print('CPF inválido')
        elif not validacoes.existeChavePrimaria('cpf', 'Clientes', cpf):
            print('CPF inexistente')
        cpf = input('Digite o CPF do cliente:')

    data = input('Digite a DATA da venda (Formato Dia/Mês/Ano):')
    while not validacoes.dataValida(data):
        print('DATA inválida')
        data = input('Digite a DATA da venda (Formato Dia/Mês/Ano):')
    data = date(int(data.split('/')[2]), int(data.split('/')[1]), int(data.split('/')[0]))
    skus = list()
    quantidades = list()
    maisProduto = True
    while maisProduto:
        sku = input('Digite o SKU do produto:')
        while (not validacoes.skuValido(sku)) or (not validacoes.existeChavePrimaria('sku', 'Produtos', int(sku))):
            if not validacoes.skuValido(sku):
                print('SKU inválido')
            elif not validacoes.existeChavePrimaria('sku', 'Produtos', sku):
                print('SKU inexistente.')
            sku = input('Digite o SKU do produto:')
        skus.append(int(sku))
        quantidade = input('Digite a QUANTIDADE do produto:')
        while not validacoes.quantidadeValida(quantidade):
            print('QUANTIDADE inválida')
            quantidade = input('Digite a QUANTIDADE do produto:')
        quantidades.append(int(quantidade))

        opcao = input('Mais algum produto? (S/N):')
        while opcao.lower() not in ['s', 'n']:
            print('Opção inválida')
            opcao = input('Mais algum produto? (S/N):')

        if opcao.lower() == 's':
            maisProduto = True
        elif opcao.lower() == 'n':
            maisProduto = False

    bancoVendas.atualizarVenda(codigo, cpf, data, skus, quantidades)
    print('Venda Atualizada.')

def excluirVenda():
    codigo = input('Digite o código da venda:')
    while (not validacoes.codigoValido(codigo)) or (not validacoes.existeChavePrimaria('codVenda','Vendas',codigo)):
        if not validacoes.codigoValido(codigo):
            print('Código inválido')
        elif not validacoes.existeChavePrimaria('codVenda','Vendas',cod):
            print('Código inexistente')
        codigo = input('Digite o código da venda:')
    codigo=int(codigo)
    bancoVendas.excluirVenda(codigo)
    print('Venda Excluída')
