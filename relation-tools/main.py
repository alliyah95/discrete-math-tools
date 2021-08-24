from general_functions import *

def main():
    display_menu()
    menu = choose_menu()
    display_breaker()

    if menu == 1:
        composite_relation_self()
    elif menu == 2:
        composite_two_relations()
    elif menu == 3:
        relation_properties()
    
    display_breaker()


def composite_relation_self():
    print("COMPOSE A RELATION WITH ITSELF".center(50))
    error_message = "Please input a positive numeric value!"
    relation = get_relation("")
    print(" How many times would you like to compose the relation with itself?")
    num_times = input_answer(error_message)
    composite = compose_relation_with_itself(relation, num_times)
    print_composite(composite)


def composite_two_relations():
    print("FIND THE COMPOSITE OF TWO RELATIONS".center(50))
    first_relation = get_relation("first")
    second_relation = get_relation("second")
    composite = compose_two_relations(first_relation, second_relation)
    print_composite(composite)


def relation_properties():
    user_set = get_main_set()
    relation = get_relation("")
    print("\nProperties of the relation")
    print("-Reflexive" if is_reflexive(user_set, relation) else "-Not reflexive")
    print("-Symmetric" if is_symmetric(relation) else "-Not symmetric")
    print("-Anti-symmetric" if is_anti_symmetric(relation) else "-Not Anti-symmetric")
    print("-Transitive" if is_transitive(relation) else "-Not Transitive")


def choose_menu():
    error_message = "Please only choose from 1 to 3!"
    print(" Choose a number from the menu")

    while True:
        menu = input_answer(error_message)
        if menu in range(1,4):
            return menu
        print(error_message)


def display_menu():
    display_breaker()
    print("DISCRETE MATH TOOLS".center(50))
    print(" [1] Compose a relation with itself\n"+
          " [2] Find the composite of two relations\n" +
          " [3] Identify the properties of a relation")
    display_breaker()


def input_answer(error_message):
    while True:
        try:
            numeric_input = int(input(" --> "))
        except ValueError:
            print(error_message)
        else:
            return numeric_input

def display_breaker():
    print("▬"*60)
 
    
main()
