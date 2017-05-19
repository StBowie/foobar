def answer(x,y):
	return (list(set(y) - set(x)) + list(set(x) - set(y)))[0]

x = [1,2]
y = [1,2,3]

print answer(x,y)