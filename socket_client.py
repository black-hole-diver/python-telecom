# Write a client-server application that uses UDP connection.
# The client should send 'Hello Server' to the server
# and the server should send back 'Hello Client' to the client

# REF: https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client

import socket


def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()