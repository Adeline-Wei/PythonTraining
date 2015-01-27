with open("count.txt") as f:
	eles = f.read().replace('\n', ' ').split(' ')
# POP THE LAST SPACE
eles.pop(len(eles)-1)

# CREATE EMPTY DIC
dic = {}

''' Method 1'''
for ele in eles:
	if ele not in dic:
		dic.update({ele:1})
	else:
		dic.update({ele:dic.get(ele)+1})

''' Method 2 '''
for ele in eles:
	if ele not in dic:
		dic[ele] = 1
	else:
		dic[ele] += 1

# PRINT IT OUT
print dic
