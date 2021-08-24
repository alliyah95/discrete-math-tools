def get_relation(text):
    print(f"\n Input {text} relation. Format: (a,b),(b,c),(c,d) - NO SPACES!")
    relation = input(" --> ")
    elements = list(relation)
    single_pair = []
    all_pairs = []
    ctr = 0

    while ctr < len(elements):
        if elements[ctr] == '(':
            if elements[ctr+1].isdigit(): elements[ctr+1] = int(elements[ctr+1])
            if elements[ctr+3].isdigit(): elements[ctr +3] = int(elements[ctr+3])
            single_pair.extend([elements[ctr+1], elements[ctr+3]])
            all_pairs.append(tuple(single_pair))
            single_pair = []
        ctr+=1

    return all_pairs


def print_composite(result):
	print("\n Composite of the relation/s ")
	ctr = 0
	print(" --> {", end='')
	while ctr < len(result):
		if ctr == len(result) - 1:
			print(result[ctr], end="}")
		else:
			print(result[ctr], end = ",")
		ctr+=1
	print()


def compose_relation_with_itself(relation, num_times):
    composite = []
    single_pair = []
    relation_one = list(relation)
    relation_two = list(relation)

    for x in range(num_times):
	    for x in relation_one:
		    for y in relation_two:
			    if y[0] == x[1]:
				    single_pair.extend([x[0], y[1]])
				    if tuple(single_pair) not in composite:
					    composite.append(tuple(single_pair))
				    single_pair = []
	    relation_two = list(composite)
	    composite = []
    return relation_two


def compose_two_relations(relation_one, relation_two):
    composite = []
    single_pair = []
    for x in relation_one:
        for y in relation_two:
            if y[0] == x[1]:
                single_pair.extend([x[0], y[1]])
                if tuple(single_pair) not in composite:
                    composite.append(tuple(single_pair))
                single_pair = []
    return composite


def get_main_set():
    print(" Input the set from which the relation was derived.\n" + 
        " Separate values with a space.")
    main_set = input(" --> ")
    main_set = set(main_set.split())
    return main_set


def is_reflexive(main_set, relation):
    to_compare = [(element, element) for element in main_set]
    return all(pair in relation for pair in to_compare)


def is_symmetric(relation):
    to_compare = [(pair[1],pair[0]) for pair in relation]
    return all(pair in relation for pair in to_compare)


def is_anti_symmetric(relation):
    if len(relation) == 1:
        return True
    else:
        for pair in relation:
            if (pair[1],pair[0]) in relation:
                if pair[1] == pair[0]:
                    continue
                else:
                    return False
            else:
                continue
        return True


def is_transitive(relation):
    if len(relation) == 1:
        return True
    else:
        for pair1 in relation:
            to_compare = [pair2 for pair2 in relation if pair2[0] == pair1[1]]
            for pair3 in to_compare:
                if (pair1[0],pair3[1]) in relation:
                    continue
                else:
                    return False
    return True