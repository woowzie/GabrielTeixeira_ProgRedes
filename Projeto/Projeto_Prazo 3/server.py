import threading, socket
from constantes import *

clients = list()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((SERVER, PORT)); server.listen(5)
        print ('recebendo conexões em: ', (SERVER, PORT))
    except:
        return '\nnão foi possível iniciar o servidor!\n'

    while True:
        client, addr = server.accept()
        print (f'\nconexão de: {addr}\n')
        clients.append(client)

        thread = threading.Thread(target=interaçao_cliente, args=[client, addr])
        thread.start()
        
def del_client(client):
    clients.remove(client)

def interaçao_cliente(client, addr):
    while True:
        try:
            msg = client.recv(512)
            broadcast(msg, client, addr)
        except:
            print(f'\nusuário {addr} desconectado.\n')
            del_client(client); break

def broadcast(msg, client, addr):
    msg = f'{addr}{msg.decode(CODE_PAGE)}'; print(msg)
    for client_item in clients:
        if client_item != client:
            try:
                client_item.send(msg.encode(CODE_PAGE))
            except:
                del_client(client_item)

main()