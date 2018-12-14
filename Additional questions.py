#sum all the numbers that made in matrix
import numpy as np

a = int(input("Enter Number : "))
A = np.matrix([[0,0,0,1],
       [1,0,1,1],
       [1,0,0,1],
        [0,0,1,0]])
totalsum = 0

for i in range(a):
    totalsum += ((np.abs(A) ** (i+1)) * np.sign(A)).sum()

print(totalsum)
