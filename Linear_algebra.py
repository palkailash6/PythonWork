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

obj = LinearAlgebra()
obj.addition_two_matrix()
