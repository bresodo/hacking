import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.connect(("localhost", 4444))
conn.send(b"Sending data")


conn.close()
