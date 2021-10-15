"""
Algorithm
1. Arrange degree sequence in descending order
2. Identify how many nodes are to be selected using the first node. If 0:
   -- Check if the elements of the degree sequence are all zeroes. If so, degree sequence is graphical [exit]. 

If > 0:
3. Remove the first node of the degree sequence
4. Check if the length of the updated degree sequence is less than or equal to the number of selected nodes. If not, degree sequence is not graphical [exit].
5. Subtract 1 from the selected nodes if the previous condition is true. 
6. Repeat
"""

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

        seq.slice()
        print(f"Sliced sequence: {seq}")

        try:
            seq.subtract_one(num_selected)
        except IndexError:
            print(f"Graph does not exist. There are less than {num_selected} nodes in the sequence.")
            break
        else:
            print(f"Subtracted one: {seq}\n")
            seq.sort()


print("Sample 1")
check_havel_hakimi(DegreeSequence([6,4,3,2,2,4,1,1]))

print("\nSample 2")
check_havel_hakimi(DegreeSequence([8,4,3,5,2,7,1,2,4,2]))

print("\nSample 3")
check_havel_hakimi(DegreeSequence([4,4,4,2,2,2,3,3,1,4]))
