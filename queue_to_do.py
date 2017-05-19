'''
Queue To Do
===========

You're almost ready to make your move to destroy the LAMBCHOP doomsday device, but the
security checkpoints that guard the underlying systems of the LAMBCHOP are going to be
a problem. You were able to take one down without tripping any alarms, which is great!
Except that as Commander Lambda's assistant, you've learned that the checkpoints are
about to come under automated review, which means that your sabotage will be discovered
and your cover blown - unless you can trick the automated review system.

To trick the system, you'll need to write a program to return the same security checksum
that the guards would have after they would have checked all the workers through.
Fortunately, Commander Lambda's desire for efficiency won't allow for hours-long lines,
so the checkpoint guards have found ways to quicken the pass-through rate. Instead of
checking each and every worker coming through, the guards instead go over everyone in
line while noting their security IDs, then allow the line to fill back up. Once they've
done that they go over the line again, this time leaving off the last worker. They
continue doing this, leaving off one more worker from the line each time but recording
the security IDs of those they do check, until they skip the entire line, at which point
they XOR the IDs of all the workers they noted into a checksum and then take off for
lunch. Fortunately, the workers' orderly nature causes them to always line up in numerical
order without any gaps.

For example, if the first worker in line has ID 0 and the security checkpoint line holds
three workers, the process would look like this:
0 1 2 /
3 4 / 5
6 / 7 8
where the guards' XOR (^) checksum is 0^1^2^3^4^6 == 2.

Likewise, if the first worker has ID 17 and the checkpoint holds four workers, the process
would look like:
17 18 19 20 /
21 22 23 / 24
25 26 / 27 28
29 / 30 31 32
which produces the checksum 17^18^19^20^21^22^23^25^26^29 == 14.

All worker IDs (including the first worker) are between 0 and 2000000000 inclusive, and the
checkpoint line will always be at least 1 worker long.

With this information, write a function answer(start, length) that will cover for the missing
security checkpoint by outputting the same checksum the guards would normally submit before
lunch. You have just enough time to find out the ID of the first worker to be checked (start)
and the length of the line (length) before the automatic review occurs, so your program must
generate the proper checksum with just those two values.
'''
#first attempts

#memory error; list too long
def answer1(start, length):
	check_length, end, lst = length, start + length**2, []
	while start < end:
		lst += [worker_id for worker_id in range(start,start + check_length)]
		check_length += -1
		start += length
	return xor(lst)

#time limit exceeded
def answer2(start, length):
	check_length, result, end = length, 0, start + length**2
	while start < end:
		result = result^xor([worker_id for worker_id in range(start,start + check_length)])
		check_length += -1
		start += length
	return xor(lst)

#time limit exceeded
def answer3(start,length):
	check_length, result, line_spot = length, 0, 0
	for x in range(start,start + length**2):
		line_spot += 1
		if line_spot <= check_length:
			result = result^x
		if line_spot >= length:
			line_spot = 0
			check_length += -1
	return result

#time limit exceeded
def answer4(start,length):
	check_length, result = length, 0
	for line in range(length):
		line_start = line * length + start
		for x in range(line_start, line_start + check_length):
			result ^= x
		check_length += -1
	return result

import time

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

def xor(start,length):
	if start == 0:
		n = length - 1
		m = n % 4
		if m == 0: return n
		elif m == 1: return 1
		elif m == 2: return n + 1
		else: return 0
	else: return xor(0,start+length)^xor(0,start)

def answer(start, length):
	# xor of 0 to b is same as xor of 0 to a xor a to b?
	result,c = 0,0
	for line in range(length):
		result ^= xor(start + line*length,length - c)
		c += 1
	return result

def test():
	assert answer(0,3) == 2, "Test Case 1 failed"
	assert answer(17,4) == 14, "Test Case 2 failed"
	return "Test cases passed"

print test()

print timedcalls(10,answer3,0,1000)
print timedcalls(10,answer4,0,1000)
print timedcalls(10,answer,0,1000)