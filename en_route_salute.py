def answer(s):
	right_walkers,salutes = 0,0
	for digit in s:
		if digit == '>': right_walkers += 1
		if digit == '<': salutes += 2*right_walkers
	return salutes

print answer("><")