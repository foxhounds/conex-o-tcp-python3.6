from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import argparse
import time

class Envia_MSG:
    def __init__(self):
        self.msg_ = ''
        self.status = True # Retorna true para def loop_true
        self.verifi = None # Vai receber socket tcp / sock_tcp

    # Vai enviar mensagem...
    def Envia(self, msg, nome_outro):
        self.msg_ = msg + '+' + nome_outro# Recebe a message
        if self.verifi != None:
            # Codifica msg...
            self.verifi.send(str.encode(self.msg_))
    # Retorn True para loop...
    def loop_true(self):
        return self.status

# Recebe conexão client ou servidor...
def aguarda(sock_tcp, tell, host='localhost', porta=666):
    destino = (host, porta)
    sock_tcp.connect(destino)# Se conecta paralelamento
    print(" ┌Conectado com usuário", destino[0])
    print(" └──Dê um Olá \(^v^)/ \n")

    while tell.loop_true():# True... pela class def

        # Envia_MSG.verifi = socket(AF_INET, SOCK_STREAM)
        tell.verifi=sock_tcp

        while tell.loop_true(): # True...
            msg = sock_tcp.recv(1024) # Recebe msg
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

# Caso não seja execultado como um modulo
if __name__ == '__main__':
    print('')
    print("""\
        Bonsoir, Friend!

            Terminal-Chat 1.0.0

    """)
    time.sleep(2)
    print(' ┌Endereço IP do outro usuário──♥')
    host = '' # Vai passar o host para tthread/aguarda

    if host == '':
        while host == '':
            host = input(' └──> ')

    # Define nome do usuário...
    print(' ┌Inserir nome do seu usuário──♥')
    name_user = input(' └──> ')
    nome_outro = name_user
    print('')

    sock_tcp = socket(AF_INET, SOCK_STREAM) # Socket de conexão
    tell = Envia_MSG() # tell = Class Envia_MSG

    # Iniciando Thread
    tthread = Thread(target=aguarda, args=(sock_tcp, tell, host))
    tthread.start()

    # Iniciando Loop q envia mensagem...
    msg = input()
    while True:
        tell.Envia(msg, nome_outro)
        msg = input()

    tthread.join()
    sock_tcp.close()
    exit()
 # Por Paulo Roberto Júnior
