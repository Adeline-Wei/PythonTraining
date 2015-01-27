with open("count.txt") as f:
	eles = f.read().replace('\n', ' ').split(' ')
eles.pop(len(eles)-1)

dic = {}
for ele in eles:
	if ele not in dic:
		dic.update({ele:1})
	else:
		dic.update({ele:dic.get(ele)+1})

print dic
