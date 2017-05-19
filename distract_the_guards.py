from collections import defaultdict
import fractions, math

def infinite_pair(g1,g2):
	x = fractions.gcd(g1,g2)
	return math.log((g1+ g2)/x,2) % 1 != 0

def infinite_pairs(banana_list):
	graph = defaultdict(lambda: [])
	lst_index = [i for i in range(len(banana_list))]
	for i in lst_index:
		for j in range(1,len(banana_list[i:])):
			if infinite_pair(banana_list[i],banana_list[i+j]):
				graph[i].append(i+j)
				graph[i+j].append(i)
	return graph, lst_index

def remaining_matches(lst, graph):
	#returns number of matches remaining in list based on graph, in same order
	result = []
	for item in lst:
		count = 0
		for match in graph[item]:
			if match in lst: count += 1
		result.append(count)
	return [x for (y,x) in sorted(zip(result,lst))]

def matching(lst):
	gamblers,unmatched_guards = [], []
	graph, lst_index = infinite_pairs(lst)
	g1, g2 = None, None
	while len(lst_index) > 0:
		#sort lst_index by remaining matches
		lst_index = remaining_matches(lst_index,graph)
		#find g1
		while g1 is None:
			if g2 is None: g1 = lst_index[0]
			else:
				for guard in graph[g2]:
					if guard in lst_index:
						g1 = guard
						break
				g2 = None
		l = [lst_index.index(match) for match in graph[g1] if match in lst_index]
		gr = [x for x in graph[g1] if x in lst_index]
		graph[g1] = [x for y,x in sorted(zip(l,gr))]
		#find g2
		for guard in graph[g1]:
			if guard in lst_index:
				g2 = guard
				gamblers += [g1,g2]
				#print g1,g2
				break
		lst_index.remove(g1)
		if g2 is not None: lst_index.remove(g2)
		else: unmatched_guards.append(g1)
		g1 = None
	return gamblers

def answer(banana_list):
	return len(banana_list) - len(matching(banana_list))

def test():
	assert answer([1,1]) == 2, "Test case 1 failed"
	assert answer([1, 7, 3, 21, 13, 19]) == 0, "Test case 2 failed"
	assert answer([1,7,7]) == 3, "Test case 3 failed"
	assert answer([1, 1, 7, 7, 3, 3, 21, 21, 13, 13, 19, 19]) == 0, "Test case 4 failed"
	return "All test cases passed"

print test()