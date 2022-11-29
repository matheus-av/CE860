def menuPrincipal():
    print('1 - Clientes')
    print('2 - Produtos')
    print('3 - Vendas')
    print('4 - Relatórios')
    print('0 - Sair')

    opcao = input('Digite o número de uma opção:')

    if opcao == 1:
        menuClientes()
    elif opcao == 2:
        menuProdutos()
    elif opcao == 3:
        menuVendas()
    elif opcao == 4:
        menuRelatorios()
    elif opcao != 0:
        print('Opção inválida')

def menuClientes():
    print('1 - Cadastrar Cliente')
    print('2 - Consultar Clientes')
    print('3 - Atualizar Cliente')
    print('4 - Excluír Cliente')
    print('0 - Sair')

    opcao = input('Digite o número de uma opção:')

    if opcao == 1:
        cadastrarClientes()
    elif opcao == 2:
        consultarClientes()
    elif opcao == 3:
        atualizarCliente()
    elif opcao == 4:
        excluirCliente()
    elif opcao != 0:
        print('Opção inválida')

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

def menuVendas():
    print('1 - Cadastrar Venda')
    print('2 - Consultar Vendas')
    print('3 - Atualizar Venda')
    print('4 - Excluír Venda')
    print('0 - Sair')

    opcao = input('Digite o número de uma opção:')

    if opcao == 1:
        cadastrarVenda()
    elif opcao == 2:
        consultarVendas()
    elif opcao == 3:
        atualizarVenda()
    elif opcao == 4:
        excluirVenda()
    elif opcao != 0:
        print('Opção inválida')

def menuRelatorios():
    print('1 - Receita total')
    print('2 - Vendas por Localidade')
    print('3 - Produtos mais vendidos')
    print('4 - Lucros e custos totais')
    print('0 - Sair')

    opcao = input('Digite o número de uma opção:')

    if opcao == 1:
        relatorioReceitaTotal()
    elif opcao == 2:
        vendasPorLocalidade()
    elif opcao == 3:
        produtosMaisVendidos()
    elif opcao == 4:
        lucrosCustosTotais()
    elif opcao != 0:
        print('Opção inválida')