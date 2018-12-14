import numpy as np
from functools import reduce
from random import randint

def solver_python(grid):
    numbers=np.arange(1,10)
    i,j = np.where(grid==0) 
    if (i.size==0):
        return(True,grid)
    else:
        i,j=i[0],j[0]    
        row = grid[i,:] 
        col = grid[:,j]
        sqr = grid[(i//3)*3:(3+(i//3)*3),(j//3)*3:(3+(j//3)*3)].reshape(9)
        values = np.setdiff1d(numbers,reduce(np.union1d,(row,col,sqr)))

        grid_temp = np.copy(grid) 

        for value in values:
            grid_temp[i,j] = value
            test = solver_python(grid_temp)
            if (test[0]):
                return(test)

        return(False,None)

example = np.array([[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0]])

example[randint(0, 9)][randint(0, 9)] = randint(0, 9)
example = solver_python(example)[1]

x = int(input("Enter Number that you want to delete: "))
for i in range (x):
    example[randint(0, 9)][randint(0, 9)] = 0

print (example)
    

