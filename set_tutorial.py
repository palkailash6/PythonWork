class setTutorial:
    def set_demo(self):
        emptySet = set()
        print(emptySet)
        non_emptySet = set([0, 1, 2, 3, "sdfd",'avc'])
        print(non_emptySet)

    def set_iterate(self,numlist):
        for num in numlist:
            print(num)
    def add_remove_from_set(self,numlist):

        numlist.add(5)
        numlist.add('kailash')
        print(numlist)

        numlist.pop()
        print(numlist)

        numlist.discard(89)
        print(numlist)

        numlist.remove(4)
        print(numlist)

        numlist.clear()
        print(numlist)

    def set_intersection(self):
        num = input("Enter the firt list:")
        num2 = input("Enter the second list:")
        data = num.split(",")
        data1 = num2.split(",")
        set1 = set(data)
        set2 = set(data1)
        # print("Intersection of two sets are:" ,set1.intersection(set2))
        print("Intersection of two sets are:", set1 & set2)

    def getUnion_difference(self,set1,set2):
        # print(set1 | set2)
        print(set1.union(set2))

        # print(set1.difference(set2))
        set_intersect = set1 & set2
        set_diffrence = set1 - set_intersect
        print(set_diffrence)

        #symmetric difference
        set_sym_dif = set1 ^ set2
        print(set_sym_dif)
        # print(set1.symmetric_difference(set2))


# obj = setTutorial()
# non_emptySet = set([0, 1, 2, 3, 4])
# obj.set_demo()
# obj.set_iterate(non_emptySet)
# obj.add_remove_from_set(non_emptySet)
# obj.set_intersection()

# set_data = set([1,2,3,4])
# set_data2 = set([5,6,3,3])
# obj.getUnion_difference(set_data,set_data2)
