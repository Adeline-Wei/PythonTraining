import socket
import struct


HOST = "vortex.labs.overthewire.org"
PORT = 5842

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("vortex.labs.overthewire.org", 5842))
# s = create_connection((HOST, PORT))

num = 0
for i in range(0, 4):
	num += struct.unpack("I", s.recv(4))[0]

s.send(struct.pack("L", num))
print s.recv(150)