import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
p_host = ('127.0.0.1', 8080)
s.bind(p_host)
s.listen()

h_clients = []

def on_conns(client):
    while True:
        data = client.recv(1000)
        mssg = data.decode('utf-8')
        for elm in h_clients:
            if (elm == client): continue
            elm.send(bytes(mssg, 'utf-8'))
        

def once_conns():
    while True:
        print('Waiting for clients...')
        client, ip = s.accept()
        h_clients.append(client)
        client.send(bytes('Server: Connected Succesfully', 'utf-8'))
        data = client.recv(1000)
        print(data.decode('utf-8'))
        t = threading.Thread(target=on_conns, args=(client,))
        t.start()
        # print('-- Its over --')


once_conns()