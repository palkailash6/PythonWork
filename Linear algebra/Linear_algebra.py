#########################Addition of two matrix:  ######################
class LinearAlgebra:

    def addition_two_matrix(self):
        print("Create the first matrix:")
        first_matrix=  obj.create_matrix()
        print("Create the Second matrix:")
        second_matrix = obj.create_matrix()
        return (obj.add_matrix_n_print(first_matrix,second_matrix))



    def create_matrix(self):
        # For creating the first matrix
        row = int(input("Enter the row size"))
        col = int(input("Enter the col size"))
        first_matrix = []
        print("Enter the entries row wise:")
        for i in range(row):
            list_row = []
            for j in range(col):
                list_row.append(int(input()))
            first_matrix.append(list_row)

        # For printing the first matrix
        print(first_matrix)
        return first_matrix

    def add_matrix_n_print(self,first_matrix,second_matrix):
        result_matrix = []
        print()
        print("Printing the addition of two matrix result::")
        # iterate through rows
        for i in range(len(first_matrix)):
            result_matrix.append([])
            # iterate through columns
            for j in range(len(first_matrix[i])):
                result_matrix[i].append(first_matrix[i][j] + second_matrix[i][j])

        # For printing the result
        print(result_matrix)

# obj = LinearAlgebra()
# obj.addition_two_matrix()

            ###########################scalar multiplication#############
class ScalarMultiplication(LinearAlgebra):
    def scalarProductMat(self, k):
        matrx1 = obj.create_matrix()

        # scalar element is multiplied
        # by the matrix
        for i in range(3):
            for j in range(3):
                matrx1[i][j] = matrx1[i][j] * k

        for i in matrx1:
            print(i)

# obj = ScalarMultiplication()
# obj.scalarProductMat(5)






########################## vector multiplication######################
import numpy as np
class VectorMultiplication:
    X = [[5, 1, 3],
         [1, 1, 1],
         [1, 2, 1]]
    Y = [1, 2, 3]

    def vectoProductMat(self):
        print("Vector multiplication is :", np.dot(obj.X, obj.Y))

# obj = VectorMultiplication()
# obj.vectoProductMat()




            ############## To find inverse of givent matrix.##########################
import numpy as np
class inverse_of_matrix:
    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]
    def toFind_inverse_matrix(self):
        print("Inverse of matrix: \n", np.linalg.inv(obj.X))

# obj = inverse_of_matrix()
# obj.toFind_inverse_matrix()


############### multiplication of matrix ################################
class Multiplication(LinearAlgebra):
    def checkingFunction(self):
        matrx1 = obj.create_matrix()
        matrx2 = obj.create_matrix()
        # result = []
        result = [[0 for x in range(3)] for y in range(3)]
        for i in range(len(matrx1)):

            # iterating by coloum by B
            for j in range(len(matrx2[0])):

                # iterating by rows of B
                for k in range(len(matrx2)):
                    result[i][j] += matrx1[i][k] * matrx2[k][j]

        for i in result:
            print(i)


#
# obj= Multiplication()
# obj.checkingFunction()




####################transpose of matrix #########################
import numpy
class MatrixTranspose(LinearAlgebra):
    def matrix_transpose(self):
        first_matrix = [[12, 7],
             [4, 5],
             [3, 8]]

        result = [[0, 0, 0],
                  [0, 0, 0]]

        # iterate through rows
        for i in range(len(first_matrix)):
            # iterate through columns
            for j in range(len(first_matrix[0])):
                result[j][i] = first_matrix[i][j]
        print("After transpose of matrix:")
        for r in result:
            print(r)

obj = MatrixTranspose()
obj.matrix_transpose()