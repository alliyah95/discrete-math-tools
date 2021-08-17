from compose_a_relation_with_itself import get_relation

def main():
    user_set = get_main_set()
    print("Input the relation:")
    relation = get_relation()

    print("\nProperties of the relation")
    print("-Reflexive" if is_reflexive(user_set, relation) else "-Not reflexive")
    print("-Symmetric" if is_symmetric(relation) else "-Not symmetric")

def get_main_set():
    main_set = set({})
    num_elements = int(input("How many elements does the main set contain? --> "))
    for i in range(num_elements):
        main_set.add(input(f"Enter element {i+1} --> "))
    return main_set

def is_reflexive(main_set, relation):
    to_compare = [(element, element) for element in main_set]
    return all(pair in relation for pair in to_compare)

def is_symmetric(relation):
    to_compare = [(pair[1],pair[0]) for pair in relation]
    return all(pair in relation for pair in to_compare)

def is_anti_symmetric():
    pass

def is_transitive():
    pass

main()
