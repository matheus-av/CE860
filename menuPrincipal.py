import menuClientes
import menuProdutos
import menuVendas
import menuRelatorios

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