#!/user/bin/python
#Filename: py_02.py


result=0

for i in range(1,4):
	for j in range(1,4):
		for k in range(1,4):
			if i!=j and i!=k and j!=k:
				print i*100+j*10+k
				result+=1

print result

