from array import array
import operator

##################### for array demonstration##############################
class ArrayDemo:
    def arrayListValues(self, arrVal):
        # first program
        print(arrVal[0])
        print(arrVal[1])
        print(arrVal[2])
        print(arrVal[3])
        print(arrVal[4])
        # second program
        print(arrVal.tolist()[::-1])
        # arrVal.reverse()
        # print(arrVal.tolist())


class DerivedDemo(ArrayDemo):
    # third program
    def toGetDuplicateVal(self,arrVal):
        print("Number of occurrences of the number 3 in the said array: " ,arrVal.count(45))

    # fourth program
    def toRemoveFirstOccurance(self, arrVal):
        print("Before remove first occurance: ", arrVal.tolist())
        arrVal.remove(45)
        print("New array: ", arrVal)



# arr = DerivedDemo()
# array_num = array('i', [1, 3, 45, 75, 45,53,45,9,96,89])
# arr.arrayListValues(array_num)
# arr.toGetDuplicateVal(array_num)
# arr.toRemoveFirstOccurance(array_num)

##################### for dictionary demonstration##############################

class DictionaryDemo:

    # sorting dict by value in ascending and descending order
    def sort_dictionary(self, arrVal):

        print('Original dictionary : ',data)
        # sorted_d = sorted(data.items(), key=operator.itemgetter(0))
        sorted_d = sorted(data.items(), key= lambda t: t[1])
        print('Dictionary in ascending order by value : ',sorted_d)

        # sorted_d = sorted(data.items(), key=operator.itemgetter(0),reverse=True)
        sorted_d = sorted(data.items(), key=lambda t: t[1] ,reverse=True)
        print('Dictionary in descending order by value : ',sorted_d)

    def add_keyTo_dict(self, arrVal):
        arrVal.update({'ram': 'sam'})
        # new_dict = {**arrVal, **{'c': 3}}
        print(arrVal)
    def get_contcat_dict(self):
        data1 = {0: 0, 1: 0}
        data2 = {2: 1, 3: 2}
        data3 = {4: 3, 5: 4}
        data4 = {}
        for pointer in (data1, data2, data3):
            data4.update(pointer)
        print(data4)

    def dict_iterator(self,argVal):
        for key,val in argVal.items():
            print("key:",key,"---->", "Value:" ,val)

    def data_dict_multiplication(self):
        number = int(input("Define input 'n' number:"))
        data_dict = dict()

        for pointer in range(1, number):
            data_dict[pointer] = pointer * pointer
        print(data_dict)


data = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
obj = DictionaryDemo()
# obj.sort_dictionary(data)
# obj.add_keyTo_dict(data)
# obj.get_contcat_dict()
# obj.dict_iterator(data)
obj.data_dict_multiplication()