from socket import *

def menu():
    print('Quais idiomas você deseja utilizar para as traduções?')
    print('''
        1 - Português -> Inglês
        2 - Português -> Francês
    ''')
    return input('Digite sua escolha: ')

def convertToBytes(string):
    return bytearray(string, 'utf-8')

def convertToString(byte):
    return str(byte, encoding = 'utf-8')

def printAvailableWords(response):
    print('\n Lista de palavras disponíveis para tradução:')
    words = response.decode().split(' ')
    for index in range(len(words) - 1):
        print('- ', words[index])

serverName = 'localhost' # maquina onde esta o servidor
serverPort = 12005 # porta que o servidor esta escutando

# cria socket cliente (AF_INET: familia de enderecos (IPV4) | SOCK_DGRAM: tipo de socket (UDP))
clientSocket = socket(AF_INET, SOCK_DGRAM)

choice = menu()
clientSocket.sendto(convertToBytes(choice),(serverName, serverPort))

response, serverAddress = clientSocket.recvfrom(2048)

# se digitar uma opcao invalida, encerra a conexao
if response.upper() == 'INVALID':
    clientSocket.close()
    exit()
else:
    printAvailableWords(response)
    
while True:
    message = input('\n Digite a palavra que deseja saber a tradução ou digite SAIR para sair: ')

    # se digitar SAIR, encerra a conexao
    if message.upper() == 'SAIR':
        clientSocket.sendto(convertToBytes('SAIR'),(serverName, serverPort))
        break

    # envia mensagem para o servidor
    clientSocket.sendto(convertToBytes(message),(serverName, serverPort))

    translation, serverAddress = clientSocket.recvfrom(2048)

    translation = convertToString(translation)

    # se digitar SAIR, encerra a conexao
    if translation == 'INVALID':
        print('Palavra não encontrada no dicionário.')
        break

    # imprime a traducao vinda do servidor
    print(message, '->', translation)

clientSocket.close()