import validacoes
import bancoVendas
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

def consultarProdutos():
    print(bancoVendas.consultarVendas())

def atualizarProduto():
    return 0 #FAZER

def excluirVenda():
    cod = input('Digite o código da venda:')
    while (not validacoes.codigoValido(cod)) or (not validacoes.existeChavePrimaria('codVenda','Vendas',cod)):
        if not validacoes.codigoValido(cod):
            print('Código inválido')
        elif not validacoes.existeChavePrimaria('codVenda','Vendas',cod):
            print('Código inexistente')
        cod = input('Digite o código da venda:')
    bancoVendas.excluirVenda(cod)
    print('Venda Excluída')
