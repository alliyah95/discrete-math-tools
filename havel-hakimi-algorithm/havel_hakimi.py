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
    
    def slice(self):
        """ Removes the first node of the sorted degree sequence"""
        self.degree_seq = self.degree_seq[1:]

    def sort(self):
        """ Sorts the degree seqeuence in descending order"""
        self.degree_seq.sort(reverse = True)

    def __str__(self):
        return "".join(str(self.degree_seq))
