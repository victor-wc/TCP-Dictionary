from socket import *

def sendAvailableWords():
    words = bytearray()

    for word in list(portToEnglish.keys()):
        words.extend((word + ' ').encode())

    connectionSocket.send(words)

def sendInvalidMessage():
    connectionSocket.send(convertToBytes('INVALID'))

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

serverPort = 12000 
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)
print('Servidor está pronto para receber...')

connectionSocket, addr = serverSocket.accept()
print ('Conectado com: ', addr)

choice, clientAddress = connectionSocket.recvfrom(2048)

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
    message, clientAddress = connectionSocket.recvfrom(2048)

    key = convertToString(message)

    # se receber SAIR, encerra a conexao
    if not message:
         break

    if key not in dictionary:
        sendInvalidMessage()

    connectionSocket.send(convertToBytes(dictionary[key]))

connectionSocket.close()

# serverSocket.close()