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

class DegreeSequence:

    def __init__(self, degree_seq):
        self.degree_seq = degree_seq

    def get_num_selected_nodes(self):
        """ Returns the number of selected nodes in the degree sequence"""
        return self.degree_seq[0] 

    def all_zeroes(self):
        """ Checks if the nodes of the degree sequence are all zeroes
            Returns true if so, otherwise false.
        """
        return all(node==0 for node in self.degree_seq)

    def subtract_one(self,num_selected):
        """ Subtracts one from the selected nodes in the degree sequence"""
        for node in range(num_selected):
            self.degree_seq[node] -= 1
    
    def slice_sequence(self):
        """ Removes the first node of the sorted degree sequence"""
        self.degree_seq = self.degree_seq[1:]

    def sort(self):
        """ Sorts the degree seqeuence in descending order"""
        self.degree_seq.sort(reverse = True)
