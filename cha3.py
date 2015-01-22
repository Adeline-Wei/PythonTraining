with open("cha3.txt") as f:
	asciis = f.read().splitlines()[0].split(' ')[2]
asciis = [asciis[i:i+8] for i in range(0, asciis.__len__(), 8)]
asciis = [int(ele, 2) for ele in asciis]
print "".join(map(chr, asciis))


# __len__() is different from sys.getsizeof()

'''
Two ways to split file into groups per 8-bit:

1.
asciis = f.read().splitlines()[0].split(' ')[2]

2.
lines = []
for i in range(0, asciis.__len__(), 8):
	lines.append(asciis[i:i+8])
print lines
'''