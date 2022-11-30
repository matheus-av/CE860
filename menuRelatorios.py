import validacoes
import bancoRelatorios
from datetime import date
def menuRelatorios():
    print('1 - Receita total')
    print('2 - Vendas por Localidade')
    print('3 - Produtos mais vendidos')
    print('4 - Lucros e custos totais')
    print('0 - Sair')

    opcao = input('Digite o número de uma opção:')

    if opcao == '1':
        relatorioReceitaTotal()
    elif opcao == '2':
        vendasPorLocalidade()
    elif opcao == '3':
        produtosMaisVendidos()
    elif opcao == '4':
        lucrosCustosTotais()
    else:
        print('Opção inválida')

def relatorioReceitaTotal():
    dataInicial = input('Digite a DATA inicial (Formato Dia/Mês/Ano):')
    while not validacoes.dataValida(dataInicial):
        print('DATA inválida')
        dataInicial = input('Digite a DATA inicial (Formato Dia/Mês/Ano):')
    dataInicial= date(int(dataInicial.split('/')[2]),int(dataInicial.split('/')[1]),int(dataInicial.split('/')[0]))

    dataFinal = input('Digite a DATA final (Formato Dia/Mês/Ano):')
    while not validacoes.dataValida(dataFinal):
        print('DATA inválida')
        dataFinal = input('Digite a DATA final (Formato Dia/Mês/Ano):')
    dataFinal= date(int(dataFinal.split('/')[2]),int(dataFinal.split('/')[1]),int(dataFinal.split('/')[0]))
    relatorio=bancoRelatorios.receitaTotal(dataInicial,dataFinal)
    if relatorio == None:
        print("Sem resultados para as datas selecionadas.")
    else:
        print(relatorio)
def vendasPorLocalidade():
    dataInicial = input('Digite a DATA inicial (Formato Dia/Mês/Ano):')
    while not validacoes.dataValida(dataInicial):
        print('DATA inválida')
        dataInicial = input('Digite a DATA inicial (Formato Dia/Mês/Ano):')
    dataInicial = date(int(dataInicial.split('/')[2]), int(dataInicial.split('/')[1]), int(dataInicial.split('/')[0]))

    dataFinal = input('Digite a DATA final (Formato Dia/Mês/Ano):')
    while not validacoes.dataValida(dataFinal):
        print('DATA inválida')
        dataFinal = input('Digite a DATA final (Formato Dia/Mês/Ano):')
    dataFinal = date(int(dataFinal.split('/')[2]), int(dataFinal.split('/')[1]), int(dataFinal.split('/')[0]))
    relatorio=bancoRelatorios.vendasPorLocalidade(dataInicial,dataFinal)
    if relatorio == None:
        print("Sem resultados para as datas selecionadas.")
    else:
        print(relatorio)

def produtosMaisVendidos():
    dataInicial = input('Digite a DATA inicial (Formato Dia/Mês/Ano):')
    while not validacoes.dataValida(dataInicial):
        print('DATA inválida')
        dataInicial = input('Digite a DATA inicial (Formato Dia/Mês/Ano):')
    dataInicial = date(int(dataInicial.split('/')[2]), int(dataInicial.split('/')[1]), int(dataInicial.split('/')[0]))

    dataFinal = input('Digite a DATA final (Formato Dia/Mês/Ano):')
    while not validacoes.dataValida(dataFinal):
        print('DATA inválida')
        dataFinal = input('Digite a DATA final (Formato Dia/Mês/Ano):')
    dataFinal = date(int(dataFinal.split('/')[2]), int(dataFinal.split('/')[1]), int(dataFinal.split('/')[0]))
    relatorio=bancoRelatorios.produtosMaisVendidos(dataInicial,dataFinal)
    if relatorio == None:
        print("Sem resultados para as datas selecionadas.")
    else:
        print(relatorio)

def lucrosCustosTotais():
    dataInicial = input('Digite a DATA inicial (Formato Dia/Mês/Ano):')
    while not validacoes.dataValida(dataInicial):
        print('DATA inválida')
        dataInicial = input('Digite a DATA inicial (Formato Dia/Mês/Ano):')
    dataInicial = date(int(dataInicial.split('/')[2]), int(dataInicial.split('/')[1]), int(dataInicial.split('/')[0]))

    dataFinal = input('Digite a DATA final (Formato Dia/Mês/Ano):')
    while not validacoes.dataValida(dataFinal):
        print('DATA inválida')
        dataFinal = input('Digite a DATA final (Formato Dia/Mês/Ano):')
    dataFinal = date(int(dataFinal.split('/')[2]), int(dataFinal.split('/')[1]), int(dataFinal.split('/')[0]))
    relatorio=bancoRelatorios.lucrosCustosTotais(dataInicial,dataFinal)
    if relatorio == None:
        print("Sem resultados para as datas selecionadas.")
    else:
        print(relatorio)
def clientesMaisAtivos():
    dataInicial = input('Digite a DATA inicial (Formato Dia/Mês/Ano):')
    while not validacoes.dataValida(dataInicial):
        print('DATA inválida')
        dataInicial = input('Digite a DATA inicial (Formato Dia/Mês/Ano):')
    dataInicial = date(int(dataInicial.split('/')[2]), int(dataInicial.split('/')[1]), int(dataInicial.split('/')[0]))

    dataFinal = input('Digite a DATA final (Formato Dia/Mês/Ano):')
    while not validacoes.dataValida(dataFinal):
        print('DATA inválida')
        dataFinal = input('Digite a DATA final (Formato Dia/Mês/Ano):')
    dataFinal = date(int(dataFinal.split('/')[2]), int(dataFinal.split('/')[1]), int(dataFinal.split('/')[0]))
    relatorio=bancoRelatorios.clientesMaisAtivos(dataInicial,dataFinal)
    if relatorio == None:
        print("Sem resultados para as datas selecionadas.")
    else:
        print(relatorio)