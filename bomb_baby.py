'''
Bomb, Baby!
===========

You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so,
you need to deploy special self-replicating bombs designed for you by the brightest scientists on
Bunny Planet. There are two types: Mach bombs (M) and Facula bombs (F). The bombs, once released
into the LAMBCHOP's inner workings, will automatically deploy to all the strategic points you've
identified and destroy them at the same time. 

But there's a few catches. First, the bombs self-replicate via one of two distinct processes: 
Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
Every Facula bomb spontaneously creates a Mach bomb.

For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and
5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle. 

Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy
the LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass
capacitors and create a singularity at the heart of the space station - not good! 

And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the
ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the
bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!) 

You need to know how many replication cycles (generations) it will take to generate the correct amount
of bombs to destroy the LAMBCHOP. Write a function answer(M, F) where M and F are the number of Mach
and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before
you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if
this can't be done! M and F will be string representations of positive integers no larger than 10^50.
For example, if M = "2" and F = "1", one generation would need to pass, so the answer would be "1".
However, if M = "2" and F = "4", it would not be possible.
'''
from __future__ import division
import math, time, sys

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

def answer(M,F):
	count, M, F = 0, int(M), int(F)
	if M < 1 or F < 1: return "impossible"
	while M > 1 or F > 1:
		if M == F: return "impossible"
		if M > F:
			if isinstance(M,long):
				multiple = (M - F - 1) // F + 1
			else:
				multiple = math.ceil((M - F)/F)
			M += -multiple * F
			count += multiple
		if F > M:
			if isinstance(F,long):
				multiple = (F - M -1) // F + 1
			else:
				multiple = math.ceil((F - M)/M)
			F += -multiple * M
			count += multiple
	return str(int(count))

def test():
	assert answer("2","1") == "1", "Test case 1 failed"
	assert answer("4","7") == "4", "Test case 2 failed"
	assert answer("2","4") == "impossible"
	return "Test cases passed"

print test()
#print answer("2","1")

print answer("10000000000000000000000000000000000000000000000000","5")