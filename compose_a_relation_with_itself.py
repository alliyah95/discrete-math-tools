def main():
	print("\n Input the relation. Format: {(a,b),(b,c),(c,d)} - NO SPACES!")
	relation = get_relation()

	print(" How many times would you like to compose the relation with itself?")
	while True:
		num = input(" --> ")
		if num.isdigit():
			break
		else:
			print(" Please enter a numeric value only!")

	solve_for_composite(relation, int(num))


def get_relation():
	relation = input(" --> ")
	elements = list(relation)
	single_pair = []
	all_pairs = []
	ctr = 0

	while ctr < len(elements):
		if elements[ctr] == '(':
			if elements[ctr+1].isdigit(): elements[ctr+1] = int(elements[ctr+1]) 
			if elements[ctr+3].isdigit(): elements[ctr+3] = int(elements[ctr+3])
			single_pair.extend([elements[ctr+1], elements[ctr+3]])
			all_pairs.append(tuple(single_pair))
			single_pair = []
		ctr+=1

	return all_pairs


def solve_for_composite(relation, num_times):
	composite = []
	single_pair = []
	relation_one = list(relation)
	relation_two = list(relation)

	for x in range(num_times-1):
		for x in relation_one:
			for y in relation_two:
				if y[0] == x[1]:
					single_pair.extend([x[0], y[1]])
					if tuple(single_pair) not in composite:
						composite.append(tuple(single_pair))
					single_pair = []
		relation_two = list(composite)
		composite = []

	print_composite(relation_two)


def print_composite(result):
	print("\n Composite of the relation ")
	ctr = 0
	print(" --> {", end='')
	while ctr < len(result):
		if ctr == len(result) - 1:
			print(result[ctr], end="}")
		else:
			print(result[ctr], end = ",")
		ctr+=1
	print()


main()