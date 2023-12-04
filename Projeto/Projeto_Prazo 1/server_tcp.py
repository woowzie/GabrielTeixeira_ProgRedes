import socket
from time import sleep
from constantes import *
print('pronto para receber mensagens...\n\n')

# criando socket, conectando a porta e definindo o num máx de conexões
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    tcp_socket.bind((HOST_SERVER, SOCKET_PORT)); tcp_socket.listen(MAX_LISTEN)
    while True:
        conexao, cliente = tcp_socket.accept()
        print('cliente conectado: ', cliente)
        while True:
            mensagem = conexao.recv(BUFFER_SIZE)
            if not mensagem: break
            print(cliente, mensagem.decode(CODE_PAGE))

            # comunicação com o cliente:
            retorno = 'a mensagem' + (f' "{mensagem.decode(CODE_PAGE)}" ') + 'foi recebida com sucesso!\n'
            conexao.send(retorno.encode(CODE_PAGE))
        print('fechando conexão com o cliente . . .', cliente); conexao.close(); sleep(5) ;break
except OSError as erro: 
    print(f'erro na execução do socket: {erro}')