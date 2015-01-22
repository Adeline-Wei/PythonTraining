''' Base64 
	File: cha4.txt
'''

with open("cha4.txt") as f:
	print f.read().splitlines()[0].split(' ')[2].decode("base64")
