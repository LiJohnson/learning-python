
f = open('google-host.dat','r')
lines = f.readlines()
domain = []

for l in lines:
	l = l.split(' ')
	if len(l) > 1 and l[1].find(".") != -1:
		domain.append(l[1].replace("\n",""))

print(len(domain))
domain = list(set(domain))
print(len(domain))

def com(a,b):
	if len(a) == len(b):
		return cmp(a,b)
	return len(a) - len(b)

domain.sort(com)

open("google-host-out.text","w").write("\n74.125.228.230\t".join(domain))
print("\n".join(domain))