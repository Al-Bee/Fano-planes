class fano:

    def __init__(self, l, h):
        self.index = 0
        spread = [i for i in range(l, h+1)]
        if len(spread) == 8:
            self.partitioned = [[spread[i], spread[i+1]] for i in range(0,7,2)]
            f_plane = {'A': 0, 'B': 1, 'C': 2, 'D': 3} # centre, top, bottom left, bottom right
            self.combinations = [self.partitioned[f_plane['A']] + self.partitioned[f_plane['B']] + self.partitioned[f_plane['C']],
                            self.partitioned[f_plane['A']] + self.partitioned[f_plane['B']] + self.partitioned[f_plane['D']],
                            self.partitioned[f_plane['B']] + self.partitioned[f_plane['C']] + self.partitioned[f_plane['D']]]
        elif len(spread) == 9:
            self.partitioned = [[spread[i], spread[i+1], spread[i+2]] for i in range(0,7,3)]
            f_plane = {'A': 0, 'B': 1, 'C': 2} # top, bottom left, bottom right
            self.combinations = [self.partitioned[f_plane['A']] + self.partitioned[f_plane['B']],
                            self.partitioned[f_plane['A']] + self.partitioned[f_plane['C']],
                            self.partitioned[f_plane['B']] + self.partitioned[f_plane['C']]]
            
        elif len(spread) == 14:
            self.partitioned = [[spread[i]%41 + 1, spread[i+1]%41 + 1] if spread[i] >= 41 else [spread[i], spread[i+1]] for i in range(0,13,2)]
            f_plane = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6} # top, mid left, mid right, centre, bottom left, bottom mid, bottom right
            self.combinations = [self.partitioned[f_plane['A']] + self.partitioned[f_plane['B']] + self.partitioned[f_plane['E']],
                            self.partitioned[f_plane['A']] + self.partitioned[f_plane['D']] + self.partitioned[f_plane['F']],
                            self.partitioned[f_plane['A']] + self.partitioned[f_plane['C']] + self.partitioned[f_plane['G']],
                            self.partitioned[f_plane['B']] + self.partitioned[f_plane['C']] + self.partitioned[f_plane['F']],
                            self.partitioned[f_plane['B']] + self.partitioned[f_plane['D']] + self.partitioned[f_plane['G']],
                            self.partitioned[f_plane['C']] + self.partitioned[f_plane['D']] + self.partitioned[f_plane['E']],
                            self.partitioned[f_plane['E']] + self.partitioned[f_plane['F']] + self.partitioned[f_plane['G']]]
            
        elif len(spread) == 21:
            self.partitioned = [[spread[i], spread[i+1], spread[i+2]] for i in range(0,19,3)]
            f_plane = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6} # top, mid left, mid right, centre, bottom left, bottom mid, bottom right
            self.combinations = [self.partitioned[f_plane['A']] + self.partitioned[f_plane['B']] + self.partitioned[f_plane['E']],
                            self.partitioned[f_plane['A']] + self.partitioned[f_plane['D']] + self.partitioned[f_plane['F']],
                            self.partitioned[f_plane['A']] + self.partitioned[f_plane['C']] + self.partitioned[f_plane['G']],
                            self.partitioned[f_plane['B']] + self.partitioned[f_plane['C']] + self.partitioned[f_plane['F']],
                            self.partitioned[f_plane['B']] + self.partitioned[f_plane['D']] + self.partitioned[f_plane['G']],
                            self.partitioned[f_plane['C']] + self.partitioned[f_plane['D']] + self.partitioned[f_plane['E']],
                            self.partitioned[f_plane['E']] + self.partitioned[f_plane['F']] + self.partitioned[f_plane['G']]]
            
        else:
            self.combinations = []

    def show_combinations(self):
        print(self.combinations)

    def get_combinations(self):
        return self.combinations
    
    def __len__(self):
        return len(self.combinations)
    
    def __iter__(self):
        return iter(self.combinations)

    def __str__(self):
        return(str(self.combinations))
    
    def __repr__(self):
        return(str(self.combinations))
    
    def set_integer(self, digit, repl):
        for i in self.combinations:
            for j in range(len(i)):
                if i[j] == digit:
                    i[j] = repl
                    

# fp_low = fano(1,14)
# fp_mid = fano(15,28)
# fp_mid_high = fano(29,42)

# fp_test = fano(1,14)
# fp_test2 = fano(15,28)
# fp_test3 = fano(29,42)

# # fp_test3.set_integer(41,1)
# # fp_test3.set_integer(42,2)

# # fp_low.show_combinations()
# # fp_mid.show_combinations()
# # fp_mid_high.show_combinations()

# fp_test.show_combinations()
# fp_test2.show_combinations()
# fp_test3.show_combinations()