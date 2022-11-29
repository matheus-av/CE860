import validacoes
import bancoProdutos

def menuProdutos():
    print('1 - Cadastrar Produto')
    print('2 - Consultar Produtos')
    print('3 - Atualizar Produto')
    print('4 - Excluír Produto')
    print('0 - Sair')

    opcao = input('Digite o número de uma opção:')

    if opcao == 1:
        cadastrarProduto()
    elif opcao == 2:
        consultarProdutos()
    elif opcao == 3:
        atualizarProduto()
    elif opcao == 4:
        excluirProduto()
    elif opcao != 0:
        print('Opção inválida')

def cadastrarProduto():
    sku = input('Digite o SKU do produto:')
    while not validacoes.skuValido(cpf):
        print('SKU inválido')
        cpf = input('Digite o SKU do produto:')

    nome = input('Digite o NOME do produto:')
    while not validacoes.nomeValido(nome):
        print('NOME inválido')
        nome = input('Digite o NOME do produto:')
    
    custo = input('Digite o CUSTO do produto:')
    while not validacoes.custoValido(custo):
        print('CUSTO inválido')
        estado = input('Digite o CUSTO do produto:')

    preco = input('Digite o PREÇO do produto:')
    while not validacoes.precoValido(preco):
        print('PREÇO inválido')
        preco = input('Digite o PREÇO do produto:')

    bancoProdutos.cadastrarProduto(sku, nome, preco, custo)
    print('Produto Cadastrado')

def consultarProdutos():
    print(bancoProdutos.consultarProdutos())

def atualizarProduto():
    sku = input('Digite o SKU do produto:')
    while not validacoes.skuValido(cpf):
        print('SKU inválido')
        cpf = input('Digite o SKU do produto:')

    nome = input('Digite o NOME do produto:')
    while not validacoes.nomeValido(nome):
        print('NOME inválido')
        nome = input('Digite o NOME do produto:')
    
    custo = input('Digite o CUSTO do produto:')
    while not validacoes.custoValido(custo):
        print('CUSTO inválido')
        estado = input('Digite o CUSTO do produto:')

    preco = input('Digite o PREÇO do produto:')
    while not validacoes.precoValido(preco):
        print('PREÇO inválido')
        preco = input('Digite o PREÇO do produto:')

    bancoProdutos.atualizarProduto(sku, nome, preco, custo)
    print('Produto Atualizado')

def excluirProduto():
    sku = input('Digite o SKU do produto:')
    while not validacoes.skuValido(cpf):
        print('SKU inválido')
        cpf = input('Digite o SKU do produto:')

    bancoProdutos.excluirProduto(sku)
    print('Produto Excluído')