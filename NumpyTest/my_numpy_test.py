"""
This script demonstrates various operations that can be performed using the NumPy library in Python.
"""

# Import the NumPy library
import numpy as np

# Create a 1D numpy array from a list
#one-dimensional array is created from a list of integers using `np.array()`. The array is then printed to the console.

array1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", array1) # Output: [1 2 3 4 5]
print("--------------")

#The script then creates a two-dimensional array, also known as a matrix, by passing a list of lists to `np.array()`.
# The matrix is then printed to the console
matrix = np.array([[1, 2], [3, 4]])
print("2D Array (Matrix):") # Output: [[1 2]
                            #          [3 4]]
print(matrix)
print("--------------")

#The script demonstrates element-wise addition and multiplication by adding and multiplying the array with a scalar (in this case, 2).
# The results are then printed to the console.
result_add = array1 + 2
print("Add 2 to each element:", result_add) # Output: [3 4 5 6 7]
print("--------------")

#the script performs matrix multiplication using the `np.dot()` function. This function returns the dot product of two arrays.
# In this case, it multiplies the matrix with itself
result_mul = array1 * 2
print("Multiply each element by 2:", result_mul)    # Output: [ 2  4  6  8 10]
print("--------------")

# Matrix multiplication
# This operation performs matrix multiplication using the np.dot() function
result_matrix_mul = np.dot(matrix, matrix)
print("Matrix multiplication:")
print(result_matrix_mul) # Output: [[ 7 10]
                            #          [15 22]]
print("--------------")

# Compute the transpose of a matrix
# The transpose of a matrix is obtained by flipping it over its diagonal
transpose = np.transpose(matrix)
print("Transpose of the matrix:")
print(transpose) # Output: [[1 3]
                    #      [2 4]]
print("--------------")

# Create a 3x3 identity matrix
# An identity matrix is a square matrix with ones on the diagonal and zeros elsewhere.
identity_matrix = np.eye(3)
print("3x3 Identity Matrix:")
print(identity_matrix) # Output: [[1. 0. 0.]
                        #          [0. 1. 0.]
                        #          [0. 0. 1.]]

print("--------------")

# Create a 3x3 matrix with random values
# This operation creates a 3x3 matrix with random values using the np.random.rand() function.
random_matrix = np.random.rand(3, 3)
print("3x3 Random Matrix:")
print(random_matrix) # Output: A 3x3 matrix with random values
print("--------------")

# Compute the mean of an array
# The mean of an array is calculated using the np.mean() function.
mean_value = np.mean(array1)
print("Mean of the array:", mean_value) # Output: 3.0
print("--------------")

# Compute the sum of an array
# The sum of an array is calculated using the np.sum() function.
sum_value = np.sum(array1)
print("Sum of the array:", sum_value) # Output: 15
print("--------------")

# Find the maximum value in an array
# The maximum value in an array is found using the np.max() function.
max_value = np.max(array1)
print("Maximum value in the array:", max_value) # Output: 5
print("--------------")

# Find the minimum value in an array
# The minimum value in an array is found using the np.min() function.
min_value = np.min(array1)
print("Minimum value in the array:", min_value) # Output: 1
print("--------------")

# Reshape an array
# The reshape() function is used to change the shape of an array.
# In this case, the script reshapes the array to a 2x3 matrix.
reshaped_array = np.append(array1, 0).reshape(2, 3)
print("Reshaped Array:")
print(reshaped_array) # Output: [[1 2 3]
                        #          [4 5 0]]
print("--------------")

# Flatten a matrix
# The flatten() function is used to flatten a matrix into a 1D array.
# In this case, the script flattens the matrix into a 1D array.
flattened_array = matrix.flatten()
print("Flattened Array:")
print(flattened_array) # Output: [1 2 3 4]
print("--------------")

# Concatenate arrays
# The concatenate() function is used to concatenate arrays along a specified axis.
# In this case, the script concatenates two arrays along the rows (axis=0).
concatenated_array = np.concatenate((array1, array1))
print("Concatenated Array:")
print(concatenated_array) # Output: [1 2 3 4 5 1 2 3 4 5]
print("--------------")

# Split an array
# The split() function is used to split an array into multiple sub-arrays.
# In this case, the script splits the concatenated array into two sub-arrays.
split_arrays = np.split(concatenated_array, 2)
print("Split Arrays:")
print(split_arrays) # Output: [array([1, 2, 3, 4, 5]), array([1, 2, 3, 4, 5])]
print("--------------")

# Save an array to a file
# The save() function is used to save an array to a file.
# In this case, the script saves the array to a text file named 'array.txt'.
np.savetxt('array.txt', array1)
print("Array saved to 'array.txt'")
print("--------------")

# Load an array from a file
# The loadtxt() function is used to load an array from a file.
# In this case, the script loads the array from the text file 'array.txt'.
loaded_array = np.loadtxt('array.txt')
print("Loaded Array:")
print(loaded_array) # Output: [1. 2. 3. 4. 5.]

print("--------------")

# Calculate the dot product of two arrays
# The dot() function is used to calculate the dot product of two arrays.
# In this case, the script calculates the dot product of two arrays.
dot_product = np.dot(array1, array1)
print("Dot Product of Arrays:", dot_product) # Output: 55
print("--------------")

# Define two arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Calculate the cross product of the two arrays
cross_product = np.cross(array1, array2)

# Print the cross product of the arrays
print("Cross Product of Arrays:")
print(cross_product)  # Expected output for these example arrays: [-3 6 -3]
print("--------------")

# Calculate the determinant of a matrix
# The det() function is used to calculate the determinant of a matrix.
# In this case, the script calculates the determinant of the matrix.
determinant = np.linalg.det(matrix)
print("Determinant of the Matrix:", determinant) # Output: -2.0000000000000004
print("--------------")

# Calculate the inverse of a matrix
# The inv() function is used to calculate the inverse of a matrix.
# In this case, the script calculates the inverse of the matrix.
inverse_matrix = np.linalg.inv(matrix)
print("Inverse of the Matrix:")
print(inverse_matrix) # Output: [[-2.   1. ]
                        #          [ 1.5 -0.5]]
print("--------------")

# Solve a system of linear equations
# The solve() function is used to solve a system of linear equations.
# In this case, the script solves a system of linear equations using matrices.
A = np.array([[2, 1], [1, 1]])
b = np.array([3, 2])
solution = np.linalg.solve(A, b)
print("Solution to the System of Equations:")
print(solution) # Output: [1. 1.]

print("--------------")

# Calculate the eigenvalues and eigenvectors of a matrix
# The eig() function is used to calculate the eigenvalues and eigenvectors of a matrix.
# In this case, the script calculates the eigenvalues and eigenvectors of the matrix.
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues of the Matrix:")
print(eigenvalues) # Output: [0.37228132 4.62771868]
print("Eigenvectors of the Matrix:")
print(eigenvectors) # Output: [[-0.82456484 -0.41597356]
                    #          [ 0.56576746 -0.90937671]]

print("--------------")

# Calculate the norm of a vector
# The norm() function is used to calculate the norm of a vector.
# In this case, the script calculates the norm of the array.
norm_value = np.linalg.norm(array1)
print("Norm of the Array:", norm_value) # Output: 7.416198487095663
print("--------------")

# Calculate the rank of a matrix
# The matrix_rank() function is used to calculate the rank of a matrix.
# In this case, the script calculates the rank of the matrix.
rank = np.linalg.matrix_rank(matrix)
print("Rank of the Matrix:", rank) # Output: 2
print("--------------")

# Calculate the singular value decomposition of a matrix
# The svd() function is used to calculate the singular value decomposition of a matrix.
# In this case, the script calculates the singular value decomposition of the matrix.
U, S, V = np.linalg.svd(matrix)
print("U (Left Singular Vectors):")
print(U) # Output: [[-0.40455358 -0.9145143 ]
         #          [-0.9145143   0.40455358]]
print("S (Singular Values):")
print(S) # Output: [5.4649857  0.36596619]
print("V (Right Singular Vectors):")

print(V) # Output: [[-0.57604844 -0.81741556]
            #          [-0.81741556  0.57604844]]

print("--------------")

# Calculate the QR decomposition of a matrix
# The qr() function is used to calculate the QR decomposition of a matrix.
# In this case, the script calculates the QR decomposition of the matrix.
Q, R = np.linalg.qr(matrix)
print("Q (Orthogonal Matrix):")
print(Q) # Output: [[-0.31622777 -0.9486833 ]
         #          [-0.9486833   0.31622777]]
print("R (Upper Triangular Matrix):")
print(R) # Output: [[-3.16227766 -4.42718872]
         #          [ 0.          0.63245553]]

print("--------------")
