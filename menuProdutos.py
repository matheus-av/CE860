import validacoes
import bancoProdutos
import pandas as pd
def menuProdutos():
    while True:
        print('1 - Cadastrar Produto')
        print('2 - Consultar Produtos')
        print('3 - Atualizar Produto')
        print('4 - Excluir Produto')
        print('0 - Sair')

        opcao = input('Digite o número de uma opção: ')

        if opcao == "1":
            cadastrarProduto()
        elif opcao == "2":
            consultarProdutos()
        elif opcao == "3":
            atualizarProduto()
        elif opcao == "4":
            excluirProduto()
        elif opcao == "0":
            break
        else:
            print('Opção inválida')

def cadastrarProduto():
    sku = input('Digite o SKU do produto a ser cadastrado: ')
    while not validacoes.skuValido(sku) or validacoes.existeChavePrimaria('sku', 'Produtos', sku):
         if not validacoes.skuValido(sku):
            print('SKU inválido')
            sku = input('Digite o SKU do produto a ser cadastrado: ')
         elif validacoes.existeChavePrimaria('sku', 'Produtos', sku):
            print('SKU já cadastrado')
            sku = input('Digite o SKU do produto a ser cadastrado: ')

    nome = input('Digite o NOME do produto a ser cadastrado: ')
    while not validacoes.ehNulo(nome):
        print('NOME inválido')
        nome = input('Digite o NOME do produto a ser cadastrado: ')

    preco = input('Digite o PREÇO do produto a ser cadastrado: ')
    while not validacoes.custoPrecoValido(preco):
        print('PREÇO inválido')
        preco = input('Digite o PREÇO do produto: ')

    custo = input('Digite o CUSTO do produto a ser cadastrado: ')
    while not validacoes.custoPrecoValido(custo):
        print('CUSTO inválido')
        custo = input('Digite o CUSTO do produto a ser cadastrado: ')

    bancoProdutos.cadastrarProduto(sku, nome, preco, custo)
    print('Produto Cadastrado')

def consultarProdutos():
    resultados=bancoProdutos.consultarProdutos()
    skus=[r[0] for r in resultados]
    nomes = [r[1] for r in resultados]
    precos = [r[2] for r in resultados]
    custos = [r[3] for r in resultados]
    dfExibir =pd.DataFrame({'SKU':skus,
                            'Nome do Produto':nomes,
                            'Preço':precos,
                            'Custo':custos
                            })
    print(dfExibir.to_string(index=False))

def atualizarProduto():
    sku = input('Digite o SKU do produto a ser atualizado: ')
    while not validacoes.skuValido(sku) or not validacoes.existeChavePrimaria('sku', 'Produtos', sku):
        if not validacoes.skuValido(sku):
            print('SKU inválido')
            sku = input('Digite o SKU do produto a ser atualizado: ')
        elif not validacoes.existeChavePrimaria('sku', 'Produtos', sku):
            print('SKU não encontrado no Banco de Dados')
            sku = input('Digite o SKU do produto a ser atualizado: ')

    nome = input('Digite o NOME do produto a ser atualizado: ')
    while not validacoes.ehNulo(nome):
        print('NOME inválido')
        nome = input('Digite o NOME do produto a ser atualizado: ')

    preco = input('Digite o PREÇO do produto a ser atualizado: ')
    while not validacoes.custoPrecoValido(preco):
        print('PREÇO inválido')
        preco = input('Digite o PREÇO do produto a ser atualizado: ')

    custo = input('Digite o CUSTO do produto a ser atualizado: ')
    while not validacoes.custoPrecoValido(custo):
        print('CUSTO inválido')
        custo = input('Digite o CUSTO do produto a ser atualizado: ')

    bancoProdutos.atualizarProduto(sku, nome, preco, custo)
    print('Produto Atualizado')

def excluirProduto():
    sku = input('Digite o SKU do produto a ser excluído: ')
    while not validacoes.skuValido(sku) or not validacoes.existeChavePrimaria('sku', 'Produtos', sku):
        if not validacoes.skuValido(sku):
            print('SKU inválido')
            sku = input('Digite o SKU do produto a ser excluído: ')
        elif not validacoes.existeChavePrimaria('sku', 'Produtos', sku):
            print('SKU não encontrado no Banco de Dados')
            sku = input('Digite o SKU do produto a ser excluído: ')

    bancoProdutos.excluirProduto(sku)
    print('Produto Excluído')
