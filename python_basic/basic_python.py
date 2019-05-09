import calendar as cal
from datetime import date
import platform
class BasicPthon:

    # This menthod get the reverse of input string.
    def reverse_string(self):
        first_name = input("Enter the first name :")
        last_name = input("Enter the last name :")
        print("Without reversing the string  :" + first_name + " " + last_name)
        name = first_name + " " + last_name
        string_reversed = name[::-1]
        print("after reversing the string    :" + string_reversed)

    # This menthod shows how to create list and tuple .
    def list_tuple_example(self):
        my_string = input("Enter the number :")
        my_list = my_string.split(",")
        print(my_list)
        print(tuple(my_list))

    # print the first and last value form given list.
    def first_n_last_string(self):
        color_list = ["Red", "Green", "White", "Black"]
        color = color_list[0::3]
        print(color)

    # illustrate the __doc__ special method uses.
    def get_doc_inbuilt_fun(self):
        print(abs.__doc__)

    # used for getting calender from given year and month.
    def get_month_calender(self):

        yy = int(input("Enter year: "))
        mm = int(input("Enter month: "))
        # display the calendar
        print(cal.month(yy, mm))

    # Getting days difference
    def days_difference(self):
        from_date = date(2019, 7, 2)
        last_date = date(2018, 7, 11)
        delta = from_date - last_date
        print(delta.days)

    # check given input values present in list or not.
    def check_values_list(self):
        value = [12, 56, 98, 74, 563, 5]
        num = int(input("Please enter a number:"))
        if (num in value):
            print("true")
        else:
            print("false")

    # printing the histogram of given list.
    def histogram(self,values ):
         for val in values:
            histValues = ''
            times = val
            while( times > 0 ):
                histValues = histValues + '*'
                # histValues += '*'
                times = times - 1
            print(histValues)

    #List concatenation
    def concatenate_list_data(self,values):
        result = ''
        for i in values:
            result = result + str(i)
        print(result)

    #finding colors set difference which is not present in list2
    def color_diff_set(self):
        color_list_1 = set(["White", "Black", "Red"])
        color_list_2 = set(["Red", "Green"])

        print(color_list_1.difference(color_list_2))

    #converting given integer to binary.
    def integer_to_bin_convert(self):
        x = 12
        print(format(x, '08b'))
        print(format(x, '010b'))

    #determine if the python shell is executing in 32bit or 64bit mode
    def determine_shell(self):
        print(platform.architecture())

    #To find minimum and maximum value from given list.
    def max_min(self,data):
        max_num = data[0]
        min_num = data[0]

        for num in data:
            if num > max_num:
                max_num = num
            elif num < min_num:
                min_num = num
        print("Maximum number : ", max_num, "Minimum number : ", min_num)


obj = BasicPthon()
# obj.reverse_string()
# obj.list_tuple_example()
# obj.first_n_last_string()
# obj.get_doc_inbuilt_fun()
# obj.get_month_calender()
# obj.days_difference()
# obj.check_values_list()
# obj.histogram([2, 1, 9, 5])
# obj.concatenate_list_data([1, 15, 2, 5])
# obj.color_diff_set()
# obj.integer_to_bin_convert()
# obj.determine_shell()
obj.max_min([185, 10, 15, 40, 0, 42, 17, 28, 75])