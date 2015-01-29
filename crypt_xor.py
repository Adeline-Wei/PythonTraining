from itertools import cycle, izip

with open("encrypt_xor.jpg", "rb") as f:
	message = f.read()

key = "doraemon"
with open("doraemon.jpg", 'w') as p:
	p.write(''.join(chr(ord(c)^ord(k)) for c, k in izip(message, cycle(key))))
