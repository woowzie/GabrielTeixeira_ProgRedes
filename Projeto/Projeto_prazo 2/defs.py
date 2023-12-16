
import requests, json

#####################################################################################################################################################################################################################

# criar função para retornar o comando que foi digitado
def retornar(comando):
    mensagem_help = ('Dificuldade com os comandos? Poxa não se preocupe relembre comigo! ^^\n\n'
                    '/info-h --> informações de hardware\n'
                    '/info-p --> lista programas instalados\n'
                    '/info-u --> informações do user logado\n' 
                    '/historic --> exibir histórico de navegação\n'
                    '/listclient --> listagem e informação dos clientes logados')

    if comando == '/info-h': return 'informações do hardware de onde está sendo executado'
    elif comando == '/listclient': return 'lista os agentes online e retorna informações como IP, HOSTNAME, usuário logado e tempo que o mesmo está online.'
    elif comando == '/info-p': return 'mostra lista dos programas instalados no sistema operacional'
    elif comando == 'historic': return 'mostra o histórico de navegação em diferentes navegadores'
    elif comando == '/info-u': return 'mostra informações detalhadas do usuário logado (UID, grupo principal/secundários, shell padrão, etc.)'
    elif comando == '/help': return mensagem_help

#####################################################################################################################################################################################################################

# criar função para verificar o texto que foi digitado e dar um retorno correspondente na def retornar()
def verificar(mensagem, chat_id, url_base):
    primeira_msg = ('Olá, seja bem vindo a Dani bot ^^ estou aqui para ajudar!\n\n'
                            'Estou disponível para lhe auxiliar com os seguintes comandos:\n\n'
                            '/info-h --> informações de hardware\n'
                            '/info-p --> lista programas instalados\n'
                            '/info-u --> informações do user logado\n' 
                            '/historic --> exibir histórico de navegação\n'
                            '/listclient --> listagem e informação dos clientes logados')
    try:
        digitado = mensagem['message']['text']
        if digitado.lower() in ['/info-p', '/info-u', '/historic', '/help', 'listclient', '/info-h']:
            return retornar(digitado)
        elif digitado == '/start': return primeira_msg
        else: return 'Oops . . . !   o_O\n\n O comando digitado não existe ou não está correto, digite "/help" caso deseje ver a tabela com os comandos disponíveis novamente.'
    except KeyError:
        return 'Infelizmente eu não consigo interpretar esse tipo de mídia   :(\n por favor insira um comando válido ou digite "/help" para visualizar a tabela com os comandos disponíveis'

####################################################################################################################################################################################################################

# criar função com objetivo de obter as mensagens enviadas ao bot

def obtendo_mensagens(update_id, url_base):
    link = f'{url_base}getUpdates?timeout=100'
    if update_id:
        link = f'{link}&offset={update_id + 1}'   
    resultado = requests.get(link)
    try:
        data = json.loads(resultado.content); return data.get('result', [])
    except json.JSONDecodeError: return []

##################################################################################################################################################################################################################
              
# criar funçãp com objetivo de responder as mensagens recebidas 

def responder_msg(resposta,chat_id,url_base):
     link_envio = f'{url_base}sendMessage?chat_id={chat_id}&text={resposta}'
     requests.get(link_envio)

