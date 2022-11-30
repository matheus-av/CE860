import validacoes
import bancoRelatorios

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

def relatorioReceitaTotal():
    return 0  # FAZER
def vendasPorLocalidade():
    return 0 #FAZER

def produtosMaisVendidos():
    return 0 #FAZER

def lucrosCustosTotais():
    return 0 #FAZER
def clientesMaisAtivos():
    return 0 #FAZER