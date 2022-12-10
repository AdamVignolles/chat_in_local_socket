# create client in localhost

import socket
import threading
from colorama import init
from termcolor import colored

init()

class message_thread(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket

    def run(self):
        while True:
            data = self.socket.recv(1024)
            data = data.decode("utf-8")
            print(colored(f"\nMessage reçu: ", "green"), colored(f"{data}\n", "magenta"))
            print("-> ", end="")

host, port = ('localhost', 12345)

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host, port))
    print(colored("Connexion établie avec le serveur", "yellow"))

    #connexion et etablissement du nom
    name = input("Entrez votre nom: ")
    info = "name"
    socket.sendall(info.encode("utf-8"))
    socket.sendall(name.encode("utf-8"))

    data = socket.recv(1024)
    print(data.decode("utf-8"))

    print(colored("Entrez votre message: ", "blue"))

    message_receved = message_thread(socket).start()

    run = True
    while run:

        data = input("->")

        if data == "/exit" or data == "/quit" or data == "/q" or data == "/e":
            info = "exit"
            socket.sendall(info.encode("utf-8"))
            socket.sendall(data.encode("utf-8"))
            message_receved.join()
            run = False
        
        else:
            
            data = f"{name} -> {data}"
            info = "message"
            socket.sendall(info.encode("utf-8"))
            socket.sendall(data.encode("utf-8"))

except ConnectionRefusedError:
    print(colored("Connexion refusée", "red"))
    print(colored("Le serveur n'est pas lancé", "red"))

except:
    print(colored("Erreur", "red"))

finally:
    print(colored("Fermeture du client", "red"))
    socket.close()