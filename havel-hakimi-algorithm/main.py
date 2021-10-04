from havel_hakimi import *

def check_havel_hakimi(seq):
    print(f"Original sequence: {seq}\n")
    seq.sort()

    while True:
        print(f"Sorted sequence: {seq}")

        num_selected = seq.get_num_selected_nodes()

        if num_selected == 0:
            if seq.all_zeroes():
                print("Graph exists.")
            else:
                print("Graph does not exist.")
            break

        seq.slice_sequence()

        try:
            seq.subtract_one(num_selected)
        except IndexError:
            print(f"Graph does not exist. There are less than {num_selected} nodes in the sequence.")
            break
        else:
            print(f"Sliced sequence: {seq}")
            print(f"Subtracted one: {seq}\n")
            seq.sort()


print("Sample 1")
check_havel_hakimi(DegreeSequence([6, 5, 4, 3, 3, 1]))

print("\nSample 2")
check_havel_hakimi(DegreeSequence([8, 5, 6, 4, 2, 3, 4, 2, 1]))
