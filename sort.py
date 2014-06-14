import random
data = []

def getNum():
	return random.randint(1,100)

def sort1(data):
	length = len(data)
	for i in range(length):
		for j in range( length - i - 1 ):
			if data[j] > data[j+1]:
				t = data[j]
				data[j] = data[j+1]
				data[j+1] = t;
	
	return data


for (i) in range(5):
	data.append( getNum() )

print (data)

print (sort1(data))