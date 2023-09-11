import numpy as np
A = np.random.rand(8,10)
B = np.random.rand(8,10)
print(A.T.shape)
print(B.shape)
#print(A.T * B)                wll give error....cause * is used for emement wise multiplication.
# print(A.T @ B, "\n")         #infix (@) operand cab be used.
print(np.dot(A.T,B))            # np.dot() function is used for matrix multiplication.
print((A.T @ B).shape)


print("list of elements of A whose values are greater than 0.5:")
print(A[A>0.5])
print("5th column of A:\n",A[:,[4]])
print("8th column of A:\n", A[:,[7]])
print("column 3rd to 7th of B:\n",B[    :, [2,3,4,5,6]])
print("rows 2nd to 5th of B: \n",B[[1,2,3,4],:])
temp = A.sum(axis=1)
print("\n")
print("mean of all summed value:",temp.mean())


