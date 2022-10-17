# Write a client-server application that uses UDP connection.
# The client should send 'Hello Server' to the server
# and the server should send back 'Hello Client' to the client

# REF: https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client

import socket

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        if str(data) == "Hello Server":
            conn.send("Hello Client".encode())
        else:    
            data = input(' -> ')
            conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()