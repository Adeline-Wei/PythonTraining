''' Binary + Octal + Decimal + Hex 
	File: seccon.txt
'''
import string

with open("seccon.txt") as f:
	asciis = f.read().splitlines()[0].split(' ')

output = ""

for ele in asciis:
	if not ele:											# None
		pass	
	elif len(ele) in [6, 7, 8]:							# Binary
		output += chr(int(ele, 2))
	elif ele[0] == "0":									# Octal
		output += chr(int(ele, 8))
	elif ele[1] in string.lowercase:					# Hex									# Hex
		output += ele.decode("Hex")
	else:												# Ascii
		output += chr(int(ele))

print output
		