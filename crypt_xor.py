''' Goal:	   	Decrypt a jpg file
	Read file: 	encrypt_xor.jpg
	Write file:	doraemon.jpg
'''

from itertools import cycle, izip

with open("encrypt_xor.jpg", "rb") as f:
	message = f.read()

key = "doraemon"
with open("doraemon.jpg", 'wb') as p:
	p.write(''.join(chr(ord(c)^ord(k)) for c, k in izip(message, cycle(key))))


'''
x = [1, 2, 3, 4, 5, 6]
y = [a, b, c, d]

--- izip ---
>>> (1,a) (2,b) (3,c) (4,d)

--- cycle ---
>>> (1,a) (2,b) (3,c) (4,d) (5,a) (6,b)

'''