from training.python_basic import InputFromUser as user_input
from copy import deepcopy
class TupleTutorial:
    # first and second program
    def createTuple(self):
        sample = 1,561,4
        print(sample)

        tuple_data = (125,520.8,"hello",False)
        print(tuple_data)


    def unpack_tuple(self):
        data = user_input.InputUser().inputValSimple()
        element = data.split(",")
        list1,list2,list3 = element
        print("list1:",'->',list1,'->',"list2:",list2,'->',"list3:",list3)


    def clone_tuple(self):

        tup_element = ("HELLO", 5, [], True,5,7,5)
        tuplex_clone = deepcopy(tup_element)

        print(tuplex_clone)
        print(tup_element)
        # to check repeated values
        print(tup_element.count(5))

    def value_exist(self):
        data = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
        print("r" in data)
        print(5 in data)

    def convert_list_toTuple(self):
        data = ["black",343]
        value = tuple(data)
        print("touple is: ", value)

    def remove_element(self):
        data = (1, 2, 3, 4, 5)
        list_val = list(data)
        list_val.remove(2)
        tup = tuple(list_val)
        print(tup)

    def sliceProgram(self):
        data = (1, 2, 3, 4, 5)
        print(data[2:4])
        print(data[:4])

    def tuple_Reverse(self):
        temp = (5, 10, 15, 20)
        revers_val = reversed(temp)
        print(tuple(revers_val))

obj = TupleTutorial()
# obj.createTuple()
# obj.unpack_tuple()
# obj.clone_tuple()
# obj.value_exist()
# obj.convert_list_toTuple()
# obj.remove_element()
# obj.sliceProgram()
obj.tuple_Reverse()