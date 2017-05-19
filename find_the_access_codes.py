'''
Find the Access Codes
=====================

In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it.
But the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose
number of passcodes changes daily. Commander Lambda gets a report every day that includes the
locks' access codes, but only she knows how to figure out which of several lists contains the
access codes. You need to find a way to determine which list contains the access codes once
you're ready to go in. 

Fortunately, now that you're Commander Lambda's personal assistant, she's confided to you that
she made all the access codes "lucky triples" in order to help her better find them in the lists.
A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With
that information, you can figure out which list contains the number of access codes that matches
the number of locks on the door when you're ready to go in (for example, if there's 5 passcodes,
you'd need to find a list with 5 "lucky triple" access codes).

Write a function answer(l) that takes a list of positive integers l and counts the number of
"lucky triples" of (lst[i], lst[j], lst[k]) where i < j < k.  The length of l is between 2 and
2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  The answer fits within a
signed 32-bit integer. Some of the lists are purposely generated without any access codes to
throw off spies, so if no triples are found, return 0. 

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the
answer 3 total.
'''
#need to get faster
import itertools, time

def timedcall(fn,*args):
	t0 = time.clock()
	result = fn(*args)
	t1 = time.clock()
	return t1-t0, result

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers)) 

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    if isinstance(n, int):
        times = [timedcall(fn,*args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn,*args)[0])
    return min(times), average(times), max(times)

def answer1(l):
	#slow AF
	triples = [triple for triple in itertools.combinations(l,3)
					if triple[2] % triple[1] == 0
					if triple[1] % triple[0] == 0]
	return len(triples)

def answer2(l):
	#doesn't handle non-unique triples; too slow
	triples = 0
	for x in range(len(l)):
		for y in range(x+1,len(l)):
			if l[y] % l[x] == 0:
				for z in range(y+1,len(l)):
					if l[z] % l[y] == 0:
						triples += 1
	return triples

#needs to be faster
def answer3(l):
	#too slow for large lists
	return len(set([(x,y,z) for x in l
				for y in l[l.index(x)+1:]
				if y % x == 0
				for z in l[l.index(y,l.index(x)+1)+1:]
				if z % y == 0
				]))

def answer4(l):
	#too slow for large lists, takes too much memory; remove duplicate efforts?
	triples = []
	a = 0
	for integer in l:
		triples += list(itertools.product([divisor for divisor in l[:a] if integer % divisor == 0]
			,[integer],
			[multiple for multiple in l[a+1:] if multiple % integer == 0]))
		a += 1
	return len(triples)

def answer5(l):
	#failed unrevealed test cases 3-5; time works; I think I have to include non-unique values?
	triples = []
	a = 0
	for integer in l:
		triples += list(itertools.product([divisor for divisor in list(set(l[:a])) if integer % divisor == 0]
			,[integer],
			[multiple for multiple in list(set(l[a+1:])) if multiple % integer == 0]))
		a += 1
	return len(set(triples))

from collections import defaultdict
def answer(l):
	c = defaultdict(int)
	triples = 0
	for k in range(len(l)):
		for j in range(k):
			if l[k] % l[j] == 0:
				c[k] += 1
				triples += c[j]
	return triples

print answer([1,1,1,1])

#work backwards and mulitply y z matches by y x matches?
#enumerate? sets? store number of matches? list of x divisors, z multiples for all y in list?
#just multiples in rest of list, function to count those; have to exclude duplicates


def test():
	l = [1, 1, 1]
	assert answer(l) == 1, "Failed Test Case 1"
	l = [1, 2, 3, 4, 5, 6]
	assert answer(l) == 3, "Failed Test Case 2"
	l = [1,3,6,9,12]
	assert answer(l) == 5, "Failed (My) Test Case 3"
	l = [12,9,6,3,1]
	assert answer(l) == 0, "Failed (My) Test Case 4"
	return "Passed all test cases"

print test()

l = [1]*2000
#print timedcalls(10,answer,l)