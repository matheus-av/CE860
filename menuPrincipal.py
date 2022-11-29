import menuClientes
import menuProdutos
import menuVendas
import menuRelatorios

def menuPrincipal():
    while int(opcao) != 0:
        print('1 - Clientes')
        print('2 - Produtos')
        print('3 - Vendas')
        print('4 - Relatórios')
        print('0 - Sair')

        opcao = input('Digite o número de uma opção:')

        if int(opcao) == 1:
            menuClientes()
        elif int(opcao) == 2:
            menuProdutos()
        elif int(opcao) == 3:
            menuVendas()
        elif int(opcao) == 4:
            menuRelatorios()
        elif int(opcao) != 0:
            print('Opção inválida')
