# netscan, testar conectividade de portas TCP e UDP em um host
import sys, os, socket

DIR_ATUAL = os.path.dirname(os.path.abspath(__file__))
arquivoCSV = os.path.join(DIR_ATUAL, 'protocolos.csv')

# abrindo arquivo csv e tratando exceções
try:
    arquivo = open(arquivoCSV, 'r', encoding='utf-8')
except FileNotFoundError:
    print(f'erro: {arquivoCSV} não foi encontrado, verifique o nome do arquivo.'); sys.exit()
except:
    print(f'erro ao abrir o arquivo: {sys.exc_info()}'); sys.exit()

# fazendo a leitura do arquivo e deixando ele da maneira ideal
novas_linhas = list()
for string in arquivo:
    elementos = string.split('", "')
    linha_definitiva = list()
    for i in elementos:
        item_final = i.strip('"\n')
        linha_definitiva.append(item_final)
    novas_linhas.append(linha_definitiva)
arquivo.close()

# transformando os números de string para inteiros e criando listas para adicionar os tipos de porta
for porta in novas_linhas: porta[0] = int(porta[0])
TCP = list(); UDP = list(); TCPUDP = list()
for string in novas_linhas:
    if string[1] == 'TCP,UDP':
        TCPUDP.append(string[0])
    elif string[1] == 'TCP':
        TCP.append(string[0])
    else:
        UDP.append(string[0])

# estabelecendo conexão com o host
try:
    strhost = input('insira o nome do host: ')
    iphost = socket.gethostbyname(strhost)
except socket.gaierror:
    print(f'erro ao obter o endereço IP do host: {socket.gaierror}'); sys.exit()
except:
    print(f'\nerro.... {sys.exc_info()}')
else:
    print('host válido')

# criando funções para testar a conectvidade dependendo do tipo de protocolo
def tcp():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.settimeout(1)
    if sock.connect_ex((iphost, port)) == 0:
        print(f'porta {port}: protocolo: TCP - {porta[2]}/ status: \033[4;30;42maberta\033[m')
    else:
        print(f'porta {port}: protocolo: TCP - {porta[2]}/ status: \033[4;30;45mfechada\033[m')
def udp():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.settimeout(1)
    if sock.connect_ex((iphost, port)) == 0:
        print(f'porta {port}: protocolo: UDP - {porta[2]}/ status: \033[4;30;42maberta\033[m')
    else:
        print(f'porta {port}: protocolo: UDP - {porta[2]}/ status: \033[4;30;45mfechada\033[m')

for porta in novas_linhas:
    port = porta[0]
    try:
        if port in TCPUDP: tcp(); udp()
        elif port in TCP: tcp()       
        elif port in UDP: udp()
    except Exception:
        print(f'erro com a verificação da porta {port}: {Exception}')
