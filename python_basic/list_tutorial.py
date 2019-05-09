# importing the another class into this class.

# from training import min_max_num as mum
# mum.MinMaxDemonstration


from training.python_basic import InputFromUser as user_input

import  operator


class list_tutorial:
    def list_sum_oprtn(self,items):
        sum_numbers = 0
        for pointer in items:
            sum_numbers += pointer
        return sum_numbers

    def list_multi(self,list):
        mul_values = 1
        for pointer in list:
            mul_values = mul_values * pointer
        return mul_values
    def get_smallest_value(self,list):

        # print(min(list))
        list.sort()
        print(list[0])

    def find_word_end_same(self,list):
        counter = 0
        for ctr in list:
            if len(ctr) > 1 and ctr[0] == ctr[-1]:
                counter = counter + 1
        print(counter)

    def sort_list_tuple(self):
        list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
        sorted_list = sorted(list,key=operator.itemgetter(1))
        print(sorted_list)

    def rmv_dup_list(self):
        input_list = user_input.InputUser().inputList_Tuple()
        list= []
        for num in input_list:
            if num not in list:
                list.append(num)
        print("After remove duplicate from list:",list)

    # Python code to clone or copy a list
    # Using list comprehension
    def clone_list(self):
        input_list = user_input.InputUser().inputList_Tuple()
        li_copy = [i for i in input_list]
        print(input_list)
        print(li_copy)

    def find_largest_word(self):
        # list_val = input("Enter list of words:").split(" ")
        list_val = user_input.InputUser().inputValString()
        n_number = int(input("Enter nth number:"))
        list =[]
        for word in list_val:
            if len(word) > n_number:
                list.append(word)
        print(list)

    def common_value_exist(self):
        list1 = [1,3,5,6,7,7]
        list2 = [ 4, 9]
        a_set = set(list1)
        b_set = set(list2)
        if len(a_set.intersection(b_set)) > 0:
            print(True)
        else:
            print(False)

    def rmv_list_from_position(self):
        val = input("Enter the list:").split(",")
        new_li = []
        for ctr in val:
            if val.index(ctr) != 0 and val.index(ctr) != 4 and val.index(ctr) != 5:
                new_li.append(ctr)
        print(new_li)


l1 = list_tutorial()
list = ['aba', 'kailash', 'maw']
# print(l1.list_sum_oprtn(list))
# print(l1.list_multi(list))
# l1.get_smallest_value(list)

# l1.find_word_end_same(list)
# l1.sort_list_tuple()
# l1.rmv_dup_list()
# l1.clone_list()
# l1.find_largest_word()
# l1.common_value_exist()
l1.rmv_list_from_position()
