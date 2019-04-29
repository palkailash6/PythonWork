import numpy

class matrix_multiplication:
    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]

    Y = [[5, 8, 1],
         [6, 7, 3],
         [4, 5, 9]]
    def two_matrix_multi(self):

       print("Two matrix multiplication:\n", numpy.dot(obj.X,obj.Y))

obj = matrix_multiplication()
obj.two_matrix_multi()