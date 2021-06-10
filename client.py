import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8080))

username = ''

def push_mmsg(server):
    while True:
        mssg = input('')
        server.send(bytes(username + ': ' + mssg, 'utf-8'))

def get_mssg(server):
    while True:
        data = server.recv(1000)
        print(data.decode('utf-8'))


def once_sv():
    global username
    username += input('Insert your username\n')
    s.send(bytes(f'{username}: is connected', 'utf-8'))
    data = s.recv(1000)
    print(data.decode('utf-8'))
    t_send = threading.Thread(target=push_mmsg, args=(s,))
    t_get = threading.Thread(target=get_mssg, args=(s,))
    t_send.start()
    t_get.start()

once_sv()