# grid array
class Grid:
    def __init__(self, matrix):  # matrix = 2D array [j][i]
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.rows = self.createRows()
        self.cols = self.createColumns()
    def createRows(self):
        self.rows = []
        for i in range(self.height):     
            row_1 = []
            for j in range(self.width):
                row_1.append(self.matrix[i][j])
            self.rows.append(row_1)
        return self.rows
    def createColumns(self):
        self.cols = []
        for j in range(self.width):
            col_1 = []    
            for i in range(self.height):
                col_1.append(self.matrix[i][j])
            self.cols.append(col_1)
        return self.cols
    def createClone(self):
        return Grid(self.matrix)
    def stepGauss(self, row = int, col = int):
        b = self.createClone()
        for i in range(row, len(self.matrix[0])):
            for j in range(len(self.matrix) - 1, col - 1, -1):
                if i != row + col:
                    c_j = b.matrix[i][col] / (self.matrix[row + col][col])
                    self.matrix[i][j] += - c_j * (b.matrix[row + col][j])
                else:
                    continue
        return self.createClone()
    def gaussJordan(self):
        objSol = self
        for index in range(len(self.cols)):
            objSol = objSol.stepGauss(0, index)
        return objSol.matrix