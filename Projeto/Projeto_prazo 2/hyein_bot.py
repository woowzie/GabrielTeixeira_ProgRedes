import requests
from defs import *

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

