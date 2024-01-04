import threading, socket, requests
from constantes import *
from defs import *

clients = list()

def main():
    bot_thread = threading.Thread(target=bot)
    bot_thread.start()

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

def bot():
    update_id = None
    token = '6829962164:AAEQm4YUovDIkWNwPUgJaZ-EMeNAe55w0vA'
    url_base = f'https://api.telegram.org/bot{token}/'

    while True:
        atualizacao = obtendo_mensagens(update_id, url_base)
        mensagens = atualizacao
        if mensagens:
            for mensagem in mensagens:
                update_id = mensagem.get('update_id', update_id)
                chat_id = mensagem['message']['from']['id']
                resposta = verificar(mensagem, chat_id, url_base)
                respondendo(resposta, chat_id, url_base)

main()
