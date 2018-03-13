import socket


TCP_IP = '192.168.2.109'
TCP_PORT = 80
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
print("primam")

data = conn.recv(BUFFER_SIZE)
print data

f = open("www/index.html", "r")

conn.send("HTTP/1.1 200 OK\r\n")

#conn.send("<!DOCTYPE html> <html lang=\"en\"> <h> TEST </h> </html>")
conn.send(f.read())

conn.close()