def main():
	print(" Input the relations. Format: {(a,b),(b,c),(c,d)} - NO SPACES! \n")
	first_rel = get_first_relation()
	second_rel = get_second_relation()
	solve_for_composite(first_rel, second_rel)


def get_first_relation():
	print(" First relation: ")
	first_rel = input(" --> ")
	elements = list(first_rel)
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


def get_second_relation():
 	print("\n Second relation: ")
 	second_rel = input(" --> ")
 	elements = list(second_rel)
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


def solve_for_composite(relation_one, relation_two):
	composite = []
	single_pair = []
	for x in relation_one:
		for y in relation_two:
			if y[0] == x[1]:
				single_pair.extend([x[0], y[1]])
				if tuple(single_pair) not in composite:
					composite.append(tuple(single_pair))
				single_pair = []

	print_composite(composite)


def print_composite(result):
	print("\n Composite of the two relations: ")
	ctr = 0
	print(" --> {", end='')
	while ctr < len(result):
		if ctr == len(result) - 1:
			print(result[ctr], end="}")
		else:
			print(result[ctr], end = ",")
		ctr+=1


main()
