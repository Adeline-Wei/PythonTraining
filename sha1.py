import hashlib
import os
import time

count = 0
print "Running..."
startTime = time.time()
while (True):
	sha1String = hashlib.sha1(os.urandom(16)).digest()
	if sha1String[0:3] == "ABC": 
		count += 1
		print "%i: %s" % (count, sha1String)
		if count == 5:
			break;
print "Runtime: %i seconds" % (time.time() - startTime)
