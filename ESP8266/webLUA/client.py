import socket

TCP_IP = '192.168.2.40'
# TCP_IP = '192.168.2.109'
#TCP_IP = 'lincangaard.servebeer.com'
TCP_PORT = 80
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

def strHeader(header):
	# data = ''
	# for head in header:
	# 	data += head + '\n'
	# return data
	return header[0]

test = ['GET / \r\n\r\n']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(strHeader(test))
data = s.recv(1024)
while data:
	print "received data:", data
	data = s.recv(1024)
s.close()
