from socket import *

def sendAvailableWords():
    words = bytearray()

    for word in list(portToEnglish.keys()):
        words.extend((word + ' ').encode())

    serverSocket.sendto(words, clientAddress)

def sendInvalidMessage():
    serverSocket.sendto(convertToBytes('INVALID'), clientAddress)

def convertToBytes(string):
    return bytearray(string, 'utf-8')

def convertToString(byte):
    return str(message, encoding = 'utf-8')

portToEnglish = {
    'enlace': 'link',
    'roteador': 'router',
    'pacote': 'packet',
    'rede': 'network',
    'protocolo': 'protocol',
    'hospedeiro': 'host',
    'mensagem': 'message',
    'propagação': 'propagation',
    'atraso': 'delay',
    'transmissão': 'transmission',
}

portToFrench = {
    'enlace': 'lien',
    'roteador': 'routeur',
    'pacote': 'paquet',
    'rede': 'réseau',
    'protocolo': 'protocole',
    'hospedeiro': 'hôte',
    'mensagem': 'message',
    'propagação': 'propagation',
    'atraso': 'retard',
    'transmissão': 'transmission',
}

serverPort = 12005 
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print('Servidor está pronto para receber...')

choice, clientAddress = serverSocket.recvfrom(2048)
print ('Enviando para: ', clientAddress)

if int(choice) == 1:
    dictionary = portToEnglish
    sendAvailableWords()
elif int(choice) == 2:
    dictionary = portToFrench
    sendAvailableWords()
else:
    sendInvalidMessage()
    exit()

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)

    key = convertToString(message)

    # se receber SAIR, encerra a conexao
    if key.upper() == 'SAIR':
        break

    if key not in dictionary:
        sendInvalidMessage()
        break

    serverSocket.sendto(convertToBytes(dictionary[key]), clientAddress)

# serverSocket.close()