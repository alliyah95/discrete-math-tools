from havel_hakimi import *

seq = DegreeSequence([2, 2, 2, 2])
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
    print(f"Sliced sequence: {seq}")

    try:
        seq.subtract_one(num_selected)
    except IndexError:
        print(f"Graph does not exist. There are less than {num_selected} nodes in the sequence.")
        break
    else:
        print(f"Subtracted one: {seq}\n")
        seq.sort()
