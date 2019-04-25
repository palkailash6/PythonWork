class StringTutorial:
    def string_manupulation(self):

        var = "hello world !!!,welcome"
        print(var.__len__())
        print(len(var))

        # dic = {}
        dic = dict()
        for element in var:
            if element not in dic:
                dic[element] = 1
            else:
                dic[element] += 1
        print(dic)


obj = StringTutorial()
obj.string_manupulation()