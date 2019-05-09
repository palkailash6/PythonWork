import textwrap
class StringTutorial:
    def string_manupulation(self):

        var = "hello world !!!,welcome"
        # print(var.__len__())
        # print(len(var))

        # dic = {}
        dic = dict()
        for element in var:
            if element not in dic:
                dic[element] = 1
            else:
                dic[element] += 1
        print(dic)

    def replace_string_inpt_value(self):
        data= "mumbai"
        char = data[0]
        data = data.replace(char, '$')
        data = char + data[1:]

        print(data)

    def change_orgnl_string(self):
        # str_value = "pu"
        # str_value = "pull"
        str_value = "pulling"
        length = len(str_value)

        if length > 2:
            if str_value[-3:] == 'ing':
                str_value += 'ly'
            else:
                str_value += 'ing'
        print(str_value)

    def find_longest_word(self):
        words_list = ["PHP", "Exercises", "Backend"]
        word_len = []
        for n in words_list:
            word_len.append((len(n), n))
        word_len.sort()
        print(word_len)
        print(word_len[-1][1])

    def input_cnvert_upper_lower(self):
        user_input = input("Enter the word/sentence:")
        print("Words in upper case: ", user_input.upper())
        print("Words in lower case:", user_input.lower())


    def sorting_inpt_str_from_str(self):
        items = input("Enter the comma seperated words:")
        words = [ word for word in items.split(",")]
        print(",".join(sorted(list(set(words)))))


    def find_substring(self):
        data = 'https://www.w3resource.com/python-exercises/string'
        print("before substring:",data)

        # / : A rsplit parameter acts as a seperator.
        # 2 : number of times split performed.
        # [0] : at index zero th value returned from splited list.

        print(data.rsplit('/', 2)[0])
        print(data.rsplit('-', 1)[0])


    def get_formated_text(self):

        sample_text = '''
          Python is a widely used high-level, general-purpose, interpreted,
          dynamic programming language. Its design philosophy emphasizes
          code readability, and its syntax allows programmers to express
          concepts in fewer lines of code than possible in languages such
          as C++ or Java.
          '''
        print(textwrap.fill(sample_text, width=100))

    def count_substring_frm_string(self):
        inpt_value = input("Ether the string values:")
        temp = inpt_value.split(" ")
        value = temp.count("ram")
        print("Count of substring is:", value)

obj = StringTutorial()
# obj.string_manupulation()
# obj.replace_string_inpt_value()
# obj.change_orgnl_string()
# obj.find_longest_word()
# obj.input_cnvert_upper_lower()
# obj.sorting_inpt_str_from_str()
# obj.find_substring()
# obj.get_formated_text()

obj.count_substring_frm_string()