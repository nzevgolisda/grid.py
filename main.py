
from Grid import Grid
array = [
    [1, 3, 3],
    [2, 4, 6],
    [3, 9, 10]
]

obj = Grid(array)

print('Starting Value : ',obj.matrix)
print(obj.gaussJordan())