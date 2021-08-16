from compose_a_relation_with_itself import get_relation

def main():
    user_set = get_main_set()
    print("Enter the relation:")
    relation = get_relation()

    if is_reflexive(user_set, relation):
        print("The relation is reflexive.")
    else:
        print("The relation is not reflexive")

def get_main_set():
    main_set = set({})
    num_elements = int(input("How many elements does the main set contain? --> "))
    for i in range(num_elements):
        main_set.add(input(f"Enter element {i+1} --> "))
    return main_set

def is_reflexive(main_set, relation):
    to_compare = [tuple((element, element)) for element in main_set]
    return all(element in relation for element in to_compare)

def is_symmetric():
    pass

def is_anti_symmetric():
    pass

def is_transitive():
    pass

main()