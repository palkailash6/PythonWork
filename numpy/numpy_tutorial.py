import numpy as num



class NumpyExample:
    def one_dimenstional_arr(self):
        #defining the data type
        data_type = num.dtype(num.int8)
        #converting numeric into one dimenstional numpy array
        val = num.array([12.23, 13.32, 100, 36.32] ,dtype= data_type)
        print(val)

    def numpy_matrix_create(self):
        matrix = num.arange(2, 11).reshape(3, 3)
        print(matrix)

    def add_sixth_in_null_vector(self):
        #creating null vector of size 10 array
        nullVector = num.zeros(10)

        print(nullVector)
        print("Update sixth value to 11")
        nullVector[6] = 11
        print(nullVector)

    def reverse_array(self):
        org_value = num.arange(12,38)
        print("Original array:",org_value)\
        # used for reversing the array
        org_value = org_value[::-1]
        print("Reverse array:",org_value )

    def two_darray_with_1(self):
        two_darr = num.ones((5, 5))
        print("Original two darray:\n", two_darr)
        print("1 on the border and 0 inside in the array: \n")

        two_darr[1:-1, 1:-1] = 0 #two_darr[row,col] ,here row--> start to end, col--> start to end
        print(two_darr)

    def put_surround_value_to_matrix(self):

        matrix = num.ones((3,3))
        print("Original array:\n",matrix)
        print("After putting 0 on the border and 1 inside in the array")
        app_value = num.pad(matrix, pad_width=1, mode='constant', constant_values=0)
        print(app_value)

    def checkerBoardPattern(self):
        mat_dmsn = int(input("Enter matrix dimension:"))
        data = num.zeros((mat_dmsn,mat_dmsn),int)
        print("Matrix is :\n",data,"\n")
        print("After creating checker board pattern:")
        data[1::2, ::2] = 1 # putting 1 on rows by increament 2, and column increamenting by 2
        data[::2, 1::2] = 1

        for i in range(mat_dmsn):
            for j in range(mat_dmsn):
                print(data[i][j], end=" ")
            print()

    def convert_tuple_list_to_array(self):
        input_list = input("Enter the list value:").split(",")
        # List to array conversion
        print("List values are: ", input_list)
        list_val = num.asarray(input_list,dtype= int)
        print("List to array convert:",list_val)
        print()

        # tuple to array conversion
        tup_val = tuple(input_list)
        print("tuple values are: ",tup_val )
        tup_val = num.asarray(tup_val,dtype=int)
        print("after convert tuple to array:",tup_val)

    def append_value_to_array(self):
        num_val = num.array(input("Enter value:").split(","),dtype= int)
        print(type(num_val))
        val = num.append(num_val, num.array(input("Enter value to be appended:"),dtype= int))
        print((type(val)))
        print("Values are:" ,val)

    def complex_real_imag(self):
        x = num.sqrt([1 + 0j])
        y = num.sqrt([0 + 1j])
        print("Original array:x ", x)
        print("Original array:y ", y)
        print("Real part of the array:")
        print(x.real)
        print(y.real)
        print("Imaginary part of the array:")
        print(x.imag)
        print(y.imag)

    def byteConsumedInArray(self):
        num_val = num.array(input("Enter value:").split(","),dtype= num.float64)
        print("Size of the array: ", num_val.size)
        print("Length of one array element in bytes: ", num_val.itemsize)
        print("Total bytes consumed by the elements of the array: ", num_val.nbytes)

    def common_value_array_numpy(self):
        num_val1 = num.array(input("Enter fist array:").split(","), dtype=int)
        num_val2 = num.array(input("Enter 2nd array:").split(","), dtype=int)
        print("Common values are:",num.intersect1d(num_val1,num_val2))

    def set_diff_two_array(self):
        num_val1 = num.array(input("Enter fist array:").split(","), dtype=int)
        num_val2 = num.array(input("Enter fist array:").split(","), dtype=int)
        print("Unique values in array1 that are not in array2:")
        print(num.setdiff1d(num_val1, num_val2))

    def set_excliusive_Array(self):
        num_val1 = num.array(input("Enter fist array:").split(","), dtype=int)
        num_val2 = num.array(input("Enter fist array:").split(","), dtype=int)
        print("Unique values that are in only one from the input arrays:")
        print(num.setxor1d(num_val1, num_val2)) # opposite of intersection

    def compare_to_matrix(self):
        num_val1 = num.array(input("Enter fist array:").split(","), dtype=int)
        num_val2 = num.array(input("Enter fist array:").split(","), dtype=int)
        print("a > b",num.greater(num_val1, num_val2))
        print("a >= b",num.greater_equal(num_val1, num_val2))
        print("a < b",num.less(num_val1, num_val2))
        print("a <= b",num.less_equal(num_val1, num_val2))

obj = NumpyExample()
# obj.one_dimenstional_arr()
# obj.numpy_matrix_create()
# obj.add_sixth_in_null_vector()
# obj.reverse_array()
# obj.two_darray_with_1()
# obj.put_surround_value_to_matrix()
# obj.checkerBoardPattern()
# obj.convert_tuple_list_to_array()
# obj.append_value_to_array()
# obj.complex_real_imag()

# obj.byteConsumedInArray()
# obj.common_value_array_numpy()
# obj.set_diff_two_array()
# obj.set_excliusive_Array()
obj.compare_to_matrix()