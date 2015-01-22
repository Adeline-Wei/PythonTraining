with open("cha1.txt") as f:
	asciis = f.read().splitlines()[0].split(' ')
print "".join(map(chr, map(int, asciis[2:])))
