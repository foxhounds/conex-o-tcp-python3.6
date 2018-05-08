from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import argparse
import time

# Classe principal
class Envia_MSG:
    def __init__(self):
        self.msg_ = ''
        self.status = True # Retorna true para def loop_true
        self.verifi = None # Vai receber socket tcp / sock_tcp

    # Vai enviar mensagem...
    def Envia(self, msg, nome_outro):
        self.msg_ = msg + '+' + nome_outro # Recebe a message
        if self.verifi != None:
            # Codifica msg...
            self.verifi.send(str.encode(self.msg_))
    # Retorn True para loop...
    def loop_true(self):
        return self.status

# Recebe conexão client ou servidor...
def aguarda(sock_tcp, tell, host='', porta=666,):
    origem = (host, porta)
    sock_tcp.bind(origem)# Se conecta paralelamento
    sock_tcp.listen(1) # Esperando

    while True:# True... pela class def
        verifi, cliente=sock_tcp.accept()
        print(" ┌Usuário com IP", cliente[0], "está conectado.")
        print(" └──Dê um Olá \(^v^)/ \n")
        # Envia_MSG.verifi = socket(AF_INET, SOCK_STREAM)
        tell.verifi=verifi

        while True: # True...
            msg = verifi.recv(1024) # Recebe msg
            if not msg:
                break
            msg = str(msg,'utf-8')
            interface(msg) # Print msg recebida

# Função de exibir msg + nome de usuário
def interface(msg):
    mesg = ''
    name = ''
    cont = 0
    for i in msg: # salva primeira variável mesg
        if i == '+':
            break
        else:
            mesg = mesg + i
            cont += 1 # Contador para Name
    name = msg[cont+1:]
    # Exibe Menssage formatada.
    print('                        ',mesg)

# Define Nome de usuário
def Name_User():
    print(' ┌Inserir nome de usuário──♥')
    name_user = input(' └──> ')
    return name_user # Retorna o nome

# Caso não seja execultado como um modulo
if __name__ == '__main__':
    # Primeira menssagem a ser exibida!
    print('')
    print("""\
        Bonsoir, Friend!

            Terminal-Chat 1.0.0

    """)
    time.sleep(2)
    print(' ┌Seu endereço IP──♥')
    host = input(' └──> ')

    if host == '':
        host = '127.0.0.1' # Define host

    sock_tcp = socket(AF_INET, SOCK_STREAM) # Socket de conexão
    tell = Envia_MSG() # tell = Class Envia_MSG

    # Define nome de usuário
    nome_outro = Name_User()

    # Iniciando Thread
    tthread = Thread(target=aguarda, args=(sock_tcp, tell, host))
    tthread.start()

    time.sleep(1)
    print("\n ┌─Iniciando servidor de chat!♥...")
    time.sleep(2)
    print(" └─Aguardando conexão no IP {}   \n".format(host))
    #time.sleep(1)

    # Iniciando Loop q envia mensagem...
    msg = input()
    while True:
        tell.Envia(msg, nome_outro)
        msg = input()

    processo.join()
    sock_tcp.close()
    exit()
