import numpy as np
# to install a library --> terminal --> pip install (library name)
x = np.array([[1,2,3,4,5], #row 0
              [6,7,8,9,4],  #row 1
              [12,4,8,4,6]]) #row 2

y= np.array([[1,2,3,4,5],
             [4,5,6,12,4],
             [1,23,45,4,7],
             [1,3,4,5,6],
             [1,3,2,3,5]])

print(x)
print(x.shape)
print(x.reshape(15))
print(np.where(y == 4))
print(np.dot(x,y))
print(x.T) # transpose
print(x.T.shape)


