'''
Given an array of bools where 3 <= width <= 50 and 3 <= height <= 9.
Determine the number of possible previous arrays that would result in the current array.
if a cell (x,y) is True, only one of cells (x,y), (x+1,y), (x,y+1), (x+1,y+1) can be True in the previous state.
All other combinations result in the cell in the current state being False.
'''
def memoize(f):
    memo = {}
    def helper(*args):
        if args not in memo:            
            memo[args] = f(*args)
        return memo[args]
    return helper

class Nebula(object):
	def __init__(self,g):
		self.g = g
		self.height = len(g)
		self.width = len(g[0])

	@memoize
	def add_one(self,x,y,tup):
		tl,bl,tr,br = tup[0],tup[1],tup[-2],tup[-1]
		if x == self.width and y == self.height:
			return (sum((tl,bl,tr,br)) != 1)^self.g[y-1][x-1]
		else:
			if None in tup or x == 0 or y == 0 or ((sum((tl,bl,tr,br)) != 1)^self.g[y-1][x-1]):
				if y == self.height:
					x, y = x + 1, 0
				else:
					y = y + 1
				return self.add_one(x,y,tup[1:]+(True,)) + self.add_one(x,y,tup[1:]+(False,))
			else:
				return 0

def answer(g):
	neb = Nebula(g)
	tup = (None,)*(neb.height+2)
	for col in range(neb.width-1,0,-1):
		neb.add_one(col,0,tup + (True,))
		neb.add_one(col,0,tup + (False,))
	return neb.add_one(0,0,tup + (True,)) + neb.add_one(0,0,tup + (False,))

def test():
	g = [[True, False, True], [False, True, False], [True, False, True]]
	assert answer(g) == 4, "Test case 1 failed"
	g = [[True, False, True, False, False, True, True, True],
			[True, False, True, False, False, False, True, False],
			[True, True, True, False, False, False, True, False],
			[True, False, True, False, False, False, True, False],
			[True, False, True, False, False, True, True, True]]
	assert answer(g) == 254, "Test case 2 failed"
	g = [[True, True, False, True, False, True, False, True, True, False],
			[True, True, False, False, False, False, True, True, True, False],
			[True, True, False, False, False, False, False, False, False, True],
			[False, True, False, False, False, False, True, True, False, False]]
	assert answer(g) == 11567, "Test case 3 failed"
	return "All test cases passed"