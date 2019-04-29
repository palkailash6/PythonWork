import numpy
class ScalarMulti:
    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]

    Y = 9
    def scalar_multi(self):
        print("Mutliplication of scalar matrix is: \n",numpy.dot(obj.X,obj.Y))


obj = ScalarMulti()
obj.scalar_multi()

