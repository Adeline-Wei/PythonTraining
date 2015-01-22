''' rot133 
	File: cha5.txt
'''

with open("cha5.txt") as f:
	print f.read().splitlines()[0][13:].encode("rot13")