# PROJETO DESIGNADO A MATÉRIA DE PROGRAMAÇÃO PARA REDES - IFRN (CRIANDO UMA APLICAÇÃO CLIENTE/SERVIDOR)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## TIPO DE SOCKET USADO:
  > Utiliza sockets TCP na comunicação CLIENTE - SERVIDOR.   
  > Por serem orientados a conexão e garantirem a ordem de entrega dos pacotes, acredito que sockets do tipo TCP se adequem bem no projeto em questão, já que irá ocorrer uma
comunicação direta e a intenção é que a integridade constante dos dados seja mantida para um bom funcionamento. 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### SOBRE O CLIENTE:
  > O projeto tem como objetivo criar um programa, que por meio de sockets TCP, estabeleça uma conexão cliente -> <- servidor.
  
  > Uma vez executado o programa, o cliente fornece o nome do usuário logado, o nome do host e e seu ip, e logo em seguida é executado em segundo plano deixando o terminal livre para o usuário.
  
  > O cliente não permite que uma segunda instância seja carregada em sua memória, e o mesmo pode optar por se remover da memória de maneira voluntária.
  
  > Caso o servidor se encontre off-line, o cliente rodará em segundo plano enquanto faz testes a cada tempo pré determinado se o servidor voltou a ficar on-line.
  
  > Enquanto estiver na memória o agente irá responder a requisições oriundas do servidor.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### SOBRE O SERVIDOR:
  > O servidor permite conexões simultâneas de vários clientes usando um socket TCP, gerenciando as conexões ativas e verificando quando um cliente fica offline.
  
  > Assim como o cliente, o servidor possui uma opção para ser removido da memória se desejado.
  
  > Não permite que uma segunda instância seja carregada na memória.
  
  > É executado em segundo plano, e deixa o terminal livre para o usuário.
  
  > O servidor executará comandos por meio de um bot no Telegram, sendo eles:
  
  		!listclient   --> lista os agentes online e retorna informações como IP, HOSTNAME, usuário logado e tempo que o mesmo está online.

  		!history      --> mostra o histórico de navegação em diferentes navegadores, funciona em clientes sendo executados tanto no windowns quanto no linux.
  
  		!userinfo     --> mostra informações detalhadas do usuário logado (UID, grupo principal/secundários, shell padrão, etc.)
  
  		!listapp      --> mostra lista dos programas instalados no servidor, funciona em clientes sendo executados tanto no windowns quanto no linux.
  
  		!hardinfo     --> mostra as informações do hardware de onde está sendo executado.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

~ Gabriel de Sousa Teixeira ^^ ~
