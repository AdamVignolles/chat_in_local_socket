# create chat server in localhost

import socket
import threading

class ThreadedServer(threading.Thread):
    def __init__(self, connexion, all_users):
        threading.Thread.__init__(self)
        self.connexion = connexion
        self.users = all_users

    def run(self):

        while True:

            data1 = self.connexion.recv(1024)
            data1 = data1.decode("utf-8")
            data2 = self.connexion.recv(1024)
            data2 = data2.decode("utf-8")
            print("data1: ", data2)
    
            if data1 == "name":
                name = data2
                print(f"{name} vient de se connecter")
                data = "Vous êtes connecté au chat"
                self.connexion.sendall(data.encode("utf-8"))
                self.users.append(name)
            
            elif data1 == "exit":
                quit = f"{name} vient de quitter le chat"
                print(f"{name} vient de se déconnecter")
                data = "Vous êtes déconnecté du chat"
                self.connexion.sendall(data.encode("utf-8"))

                for user in self.users:
                    if user != self.connexion:
                        user.sendall(quit.encode("utf-8"))
                        
                
                self.users.remove(self.connexion)
                self.connexion.close()
                break

            

            else:
                #send message to all users
                for user in self.users:
                    msg = f"{data2}"
                    user.sendall(msg.encode("utf-8"))

host, port = ('', 12345)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print(f"Serveur Prêt sur le port {port}")

socket.listen(5)
client_connectee = True

all_users = []

while client_connectee:

    #wait for a connection
    print("Serveur en attente de connexion")
    connexion, address = socket.accept()
    print(f"Connexion de {address}")
    all_users.append(connexion)
    ThreadedServer(connexion, all_users).start()
    if connexion == None:
        client_connectee = False

socket.close()

    