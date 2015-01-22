with open("cha3.txt") as f:
	asciis = f.read().splitlines()[0].split(' ')[2]
length = len(str(asciis))
asciis = [asciis[i:i+8] for i in range(0, length, 8)]
asciis = [int(ele, 2) for ele in asciis]
print "".join(map(chr, asciis))