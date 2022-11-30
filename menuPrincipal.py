import menuClientes
import menuProdutos
import menuVendas
import menuRelatorios

def menuPrincipal():
    while True:
        print('1 - Clientes')
        print('2 - Produtos')
        print('3 - Vendas')
        print('4 - Relatórios')
        print('0 - Sair')
        
        opcao = input('Digite o número de uma opção:')
        
        if opcao == "1":
            menuClientes.menuClientes()
        elif opcao == "2":
            menuProdutos.menuProdutos()
        elif opcao == "3":
            menuVendas.menuVendas()
        elif opcao == "4":
            menuRelatorios.menuRelatorios()
        elif opcao == "0":
            print('Programa finalizado')
            break
        else:
            print('Opção inválida')
