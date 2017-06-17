class Puzzle():
    def __init__(self, n_cols=14, n_rows=24):
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.cells = [[False for _ in xrange(n_rows)] for _ in xrange(n_cols)]

    def __getitem__(self, key):
        try:
            if type(key) is tuple:
                # If key is a tuple, it should be an index (x,y) for a cell
                assert len(key) == 2, key
                return self[key[0]][key[1]]
            else:
                # Otherwise key should be a numeric index to a column
                return self.cells[key]
        except AssertionError, argument:
            err_str = 'tuple ' + str(argument)
            err_str += ' is an illegal index to Puzzle class'
            raise ValueError, err_str
