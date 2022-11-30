import validacoes
import bancoClientes

def menuClientes():
    while True:
        print('1 - Cadastrar Cliente')
        print('2 - Consultar Clientes')
        print('3 - Atualizar Cliente')
        print('4 - Excluír Cliente')
        print('0 - Sair')

        opcao = input('Digite o número de uma opção:')

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
    cpf = input('Digite o CPF do cliente:')
    while not validacoes.cpfValido(cpf):
        print('CPF inválido')
        cpf = input('Digite o CPF do cliente:')

    nome = input('Digite o NOME do cliente:')
    while not validacoes.nomeValido(nome):
        print('NOME inválido')
        nome = input('Digite o NOME do cliente:')
    
    estado = input('Digite o ESTADO do cliente:')
    while not validacoes.estadoValido(estado):
        print('ESTADO inválido')
        estado = input('Digite o ESTADO do cliente:')

    bancoClientes.cadastrarCliente(cpf, nome, estado)
    print('Cliente Cadastrado')

def consultarClientes():
    print(bancoClientes.consultarClientes())

def atualizarCliente():
    cpf = input('Digite o CPF do cliente:')
    while not validacoes.cpfValido(cpf):
        print('CPF inválido')
        cpf = input('Digite o CPF do cliente:')

    nome = input('Digite o NOME do cliente:')
    while not validacoes.nomeValido(nome):
        print('NOME inválido')
        nome = input('Digite o NOME do cliente:')
    
    estado = input('Digite o ESTADO do cliente:')
    while not validacoes.estadoValido(estado):
        print('ESTADO inválido')
        estado = input('Digite o ESTADO do cliente:')

    bancoClientes.atualizarCliente(cpf, nome, estado)
    print('Cliente Atualizado')

def excluirCliente():
    cpf = input('Digite o CPF do cliente:')
    while not validacoes.cpfValido(cpf):
        print('CPF inválido')
        cpf = input('Digite o CPF do cliente:')

    bancoClientes.excluirCliente(cpf)
    print('Cliente Excluído')
