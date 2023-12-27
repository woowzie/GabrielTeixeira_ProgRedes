# solicitar url de uma imagem e fazer o download dela no dir atual com o mesmo nome contido na url
import socket
port = 80

# obter nome do arquivo
def nome_url(url):
    url_partes = url.split('/')
    return url_partes[-1]

try:
    url_completa = input('digite a URL da imagem: ')

    # pegando o nome da imagem
    url_dividida = url_completa.split('//')
    url_host = url_dividida[1].split('/')[0]
    url_image = '/' + '/'.join(url_dividida[1].split('/')[1:])
    nome_arquivo = nome_url(url_completa)
    print (f'{nome_arquivo}')

    # criando socket
    url_request = f'GET {url_image} HTTP/1.1\r\nHost: {url_host}\r\n\r\n'
    sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM); sock_img.connect((url_host, port))
    sock_img.sendall(url_request.encode())

    content_length = None
    imagem = b''

    # tratando possíveis erros 
    if '.' not in nome_arquivo or nome_arquivo.split('.')[-1] not in ['png', 'jpg', 'jpeg']:
        nome_arquivo += '.png'

    while True:

        # recebendo os dados em 5120 bytes
        dados = sock_img.recv(5120)
        if not dados: break
        imagem += dados

        # buscando contentlenght
        busca_cl = imagem.split(b'Content-Length:')
        if len(busca_cl) > 1:
            content_length = int(busca_cl[1].split()[0])

        # verificando se os dados chegaram corretamente
        if len(imagem) >= content_length and content_length is not None: break

    sock_img.close()
    print(f'\n a imagem possui {content_length} bytes')

    # separando dados e cabeçalho
    delimiter = '\r\n\r\n'.encode();    position = imagem.find(delimiter)
    headers = imagem[:position];        dadosbin = imagem[position + 4:]

    # Salva a imagem no arquivo
    file_output = open(nome_arquivo, 'wb')
    file_output.write(dadosbin); file_output.close()

except TimeoutError: print('o tempo de espera foi excedido')
except ConnectionError: print('erro ao conectar')
except Exception as erro: print(f'ERRO . . . {erro}')



