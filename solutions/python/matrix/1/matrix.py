class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        for row_str in matrix_string.split('\n'):
            row = map(int, row_str.split())
            self.matrix.append(row)

    def row(self, index):
        return self.matrix[index].copy()

    def column(self, index):
        return [row[index] for row in self.matrix]
