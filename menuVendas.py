import validacoes
import bancoVendas

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
    cpf = input('Digite o CPF do cliente:')
    while not validacoes.cpfValido(cpf):
        print('CPF inválido')
        cpf = input('Digite o CPF do produto:')

    data = input('Digite a DATA da venda:')
    while not validacoes.dataValida(data):
        print('DATA inválida')
        nome = input('Digite a DATA da venda:')
    
    maisProduto = True
    while maisProduto:
        
        sku = input('Digite o SKU do produto:')
        while not validacoes.skuValido(sku):
            print('SKU inválido')
            sku = input('Digite o SKU do produto:')

        quantidade = input('Digite a QUANTIDADE do produto:')
        while not validacoes.quantidadeValida(quantidade):
            print('QUANTIDADE inválida')
            preco = input('Digite a QUANTIDADE do produto:')
        
        opcao = input('Mais algum produto? (S/N):')
        while opcao.lower() not in ['s', 'n']:
            print('Opção inválida')
            opcao = input('Mais algum produto? (S/N):')

        if opcao.lower() == 's':
            maisProduto = True
        elif opcao.lower() == 'n':
            maisProduto = False
        
    bancoVendas.cadastrarVenda()
    print('Venda Cadastrada')

def consultarProdutos():
    print(bancoVendas.consultarVendas())

def atualizarProduto():
    return 0 #FAZER

def excluirProduto():
    return 0 #FAZER
