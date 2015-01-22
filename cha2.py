with open("cha2.txt") as f:
	asciis = f.read().splitlines()[0].split(':')
print "".join(asciis[1:]).strip(' ').decode("hex")