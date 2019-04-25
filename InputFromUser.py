class InputUser:

    def inputFromUser(self):
        input_values = []

        input_values.append(input("Enter the first list:"))
        input_values.append(input("Enter the second list:"))

        return str(input_values)
    def inputFromUser_list(self):
        input_values = []

        l1 = input("Enter the first list:")
        l2 = input("Enter the second list:")

        return l1,l2

    def inputList_Tuple(self):
        my_string = input("Enter the number :")
        my_list = my_string.split(",")
        print(type(my_list))
        return my_list

    def inputValString(self):
        my_string = input("Enter the value :").split(" ")
        return my_string

    def inputValSimple(self):
        my_string = input("Enter the value :")
        return my_string
# obj = InputUser()
# print(obj.inputFromUser())