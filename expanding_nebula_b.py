import cProfile
import itertools
from collections import defaultdict

def memoize(f):
    memo = {}
    def helper(*args):
        if args not in memo:            
            memo[args] = f(*args)
        return memo[args]
    return helper

class Nebula(object):
	def __init__(self,g):
		bools = {True,False}
		self.g = g
		self.height = len(g)
		self.width = len(g[0])
		self.columns = set(itertools.product(bools,repeat=self.height+1))
		self.counts = defaultdict(lambda:1)

	@memoize
	def evolve(self,col1,col2):
		gcol = ()
		for y in xrange(self.height):
			tl = col1[y]
			bl = col1[y+1]
			tr = col2[y]
			br = col2[y+1]
			cell = sum((tl,bl,tr,br)) == 1
			gcol += (cell,)
		return gcol

	@memoize
	def column(self,x):
		col = ()
		for y in xrange(self.height):
			col += (self.g[y][x],)
		return col

	def count(self,x):
		dct = defaultdict(int)
		for col1 in self.columns:
			for col2 in self.columns:
				if self.evolve(col1,col2) == self.column(x):
					dct[col2] += self.counts[col1]
		self.counts = dct

	def total(self):
		for x in xrange(self.width):
			self.count(x)
		return sum(self.counts.itervalues())

def answer(g):
	neb = Nebula(g)
	return neb.total()

def prof_test():
	g = [[True,True,True,True],
			[True,True,True,True],
			[True,True,True,True],
			[True,True,True,True],
			[True,True,True,True],
			[True,True,True,True],
			[True,True,True,True],
			[True,True,True,True],
			[True,True,True,True],
			[True,True,True,True]]
	neb = Nebula(g)
	return neb.total()

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

print test()
'''print answer([[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
				[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
				[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
				[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
				[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
				[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
				[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
				[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
				[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],
				[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]])'''

cProfile.run('test()')