import validacoes
import bancoClientes
import pandas as pd
def menuClientes():
    while True:
        print('1 - Cadastrar Cliente')
        print('2 - Consultar Clientes')
        print('3 - Atualizar Cliente')
        print('4 - Excluir Cliente')
        print('0 - Sair')

        opcao = input('Digite o número de uma opção: ')

        if opcao == "1":
            cadastrarCliente()
        elif opcao == "2":
            consultarClientes()
        elif opcao == "3":
            atualizarCliente()
        elif opcao == "4":
            excluirCliente()
        elif opcao == "0":
            break
        else:
            print('Opção inválida')

def cadastrarCliente():
    cpf = input('Digite o CPF do cliente a ser cadastrado: ')
    while not validacoes.cpfValido(cpf) or validacoes.existeChavePrimaria('cpf', 'Clientes', cpf):
        if not validacoes.cpfValido(cpf):
            print('CPF inválido')
            cpf = input('Digite o CPF do cliente a ser cadastrado: ')
        if validacoes.existeChavePrimaria('cpf', 'Clientes', cpf):
            print('CPF já cadastrado')
            cpf = input('Digite o CPF do cliente a ser cadastrado: ')

    nome = input('Digite o NOME do cliente a ser cadastrado: ')
    while not validacoes.ehNulo(nome):
        print('NOME inválido')
        nome = input('Digite o NOME do cliente a ser cadastrado: ')
    
    estado = input('Digite o ESTADO do cliente a ser cadastrado: ')
    while not validacoes.estadoValido(estado):
        print('ESTADO inválido')
        estado = input('Digite o ESTADO do cliente a ser cadastrado: ')

    bancoClientes.cadastrarCliente(cpf, nome, estado)
    print('Cliente Cadastrado')

def consultarClientes():
    resultados = bancoClientes.consultarClientes()
    cpfs = [r[0] for r in resultados]
    nomes = [r[1] for r in resultados]
    estados = [r[2] for r in resultados]
    dfExibir = pd.DataFrame({'CPF': cpfs,
                             'Nome do Cliente': nomes,
                             'Estado': estados,
                             })
    print(dfExibir.to_string(index=False))

def atualizarCliente():
    cpf = input('Digite o CPF do cliente a ser atualizado: ')
    while not validacoes.cpfValido(cpf) or not validacoes.existeChavePrimaria('cpf', 'Clientes', cpf):
        if not validacoes.cpfValido(cpf):
            print('CPF inválido')
            cpf = input('Digite o CPF do cliente a ser atualizado: ')
        if not validacoes.existeChavePrimaria('cpf', 'Clientes', cpf):
            print('CPF não encontrado no Banco de Dados')
            cpf = input('Digite o CPF do cliente a ser atualizado: ')

    nome = input('Digite o NOME do cliente a ser atualizado:')
    while not validacoes.ehNulo(nome):
        print('NOME inválido')
        nome = input('Digite o NOME do cliente a ser atualizado: ')
    
    estado = input('Digite o ESTADO do cliente a ser atualizado: ')
    while not validacoes.estadoValido(estado):
        print('ESTADO inválido')
        estado = input('Digite o ESTADO do cliente a ser atualizado: ')

    bancoClientes.atualizarCliente(cpf, nome, estado)
    print('Cliente Atualizado')

def excluirCliente():
    cpf = input('Digite o CPF do cliente a ser excluído: ')
    while not validacoes.cpfValido(cpf) or not validacoes.existeChavePrimaria('cpf', 'Clientes', cpf):
        if not validacoes.cpfValido(cpf):
            print('CPF inválido')
            cpf = input('Digite o CPF do cliente a ser excluído: ')
        if not validacoes.existeChavePrimaria('cpf', 'Clientes', cpf):
            print('CPF não encontrado no Banco de Dados')
            cpf = input('Digite o CPF do cliente a ser excluído: ')

    bancoClientes.excluirCliente(cpf)
    print('Cliente Excluído')
