import socket
from constantes import *

# criando socket tcp e o conectando com a porta desejada
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    tcp_socket.connect((HOST_SERVER, SOCKET_PORT))
    print('conectado ao servidor com sucesso!')
    print('digite "!q" para encerrar conexão.\n\n')
# cliente se comunica com o servidor e recebe resposta
    while True:
        mensagem = input('envie uma mensagem: ')
        if mensagem == '!q': break
        elif mensagem:
            mensagem = mensagem.encode(CODE_PAGE)
            tcp_socket.send(mensagem)

            # recebendo resposta do server
            dado_recebido     = tcp_socket.recv(BUFFER_SIZE)
            mensagem_recebida = dado_recebido.decode(CODE_PAGE)
            print(mensagem_recebida)
except OSError as erro:
    print(f'erro na conexão do socket: {erro}')
tcp_socket.close()