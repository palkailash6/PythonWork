# @author  Kailash Pal
# @version 1.0
# Simple class for demonstrating the Matplolib.

# importing the libraries.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Parent class
class IputDataClass:
    def __init__(self):
        #initialize input through constructor.
        self.lang = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
        self.popular = [10, 8, 6, 14, 2, 1]

    def inputPassFuc(self):
        #Assigning value and returting to method.
        language = self.lang
        popularity = self.popular
        return language,popularity

#Child class
class BarchartTutorial(IputDataClass):
    def __init__(self):
        IputDataClass.__init__(self)

    def simple_bar_chart(self):

        #Created object of parent class for initializing input.
        inputObj = IputDataClass()
        data = inputObj.inputPassFuc()
        List_data = list(data)
        lang = List_data[0]
        populr = List_data[1]
        x_pos = np.arange(len(lang))

        #visualization
        plt.bar(x_pos, populr, align='center', alpha=0.5)
        plt.xticks(x_pos, lang)
        plt.xlabel("Lunguages")
        plt.ylabel('Popularity')
        plt.title('Programming language Popularity')

        # plt_barchart = obj.create_bar_chart()
        plt.show()

    #visualization of barcharts horizontally.
    def horizontal_barchart(self):
        # Created object of parent class for initializing input.
        inputObj = IputDataClass()
        data = inputObj.inputPassFuc()
        List_data = list(data)
        lang = List_data[0]
        populr = List_data[1]
        x_pos = np.arange(len(lang))

        # visualization
        plt.barh(x_pos, populr, color='green')
        plt.xlabel("Popularity")
        plt.ylabel("Languages")
        plt.title("Popularity of Programming Language")
        plt.yticks(x_pos, lang) # plotting horizontal graph.
        # Turn on the grid
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        # Customize the minor grid
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.show()

    #visualization of barchart with uniform color.
    def uniform_color_barchart(self):
        languages = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
        y_pos = np.arange(len(languages))
        popularity = [10, 8, 6, 4, 2, 1]
        plt.bar(y_pos, popularity, align='center', alpha=0.5,color ='red') # color attirbute used for setting uniform color.
        plt.xticks(y_pos, languages)
        plt.xlabel("Lunguages")
        plt.ylabel('Popularity')
        plt.title('Programming language Popularity')
        plt.show()

    #visualization of bars with diffrent colors.
    def different_color_barchart(self):
        languages = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
        y_pos = np.arange(len(languages))
        popularity = [10, 8, 6, 4, 2, 1]
        plt.bar(y_pos, popularity, align='center', alpha=0.5,color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])  # color attirbute used for setting uniform color.
        plt.xticks(y_pos, languages)
        plt.xlabel("Lunguages")
        plt.ylabel('Popularity')
        plt.title('Programming language Popularity')
        plt.show()

    #text on barchart displaying.
    def text_on_barchart(self):
        launguages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        x_pos = [i for i, _ in enumerate(launguages)]
        print(x_pos)

        fig, ax = plt.subplots()
        rects1 = ax.bar(x_pos, popularity, color='b')
        plt.xlabel("Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language 2017 compared to a year ago")
        plt.xticks(x_pos, launguages)
        # Turn on the grid
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        # Customize the minor grid
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

        def autolabel(rects):
            """
            Attach a text label above each bar displaying its height
            """
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,'%f' % float(height),ha='center', va='bottom')

        autolabel(rects1)

        plt.show()

    #blue border visualization of bars
    def blue_border_barchart(self):
        languages = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
        y_pos = np.arange(len(languages))
        popularity = [10, 8, 6, 4, 2, 1]
        plt.bar(y_pos, popularity, align='center', alpha=0.5, color='red',edgecolor = 'b')  # edgecolor attirbute used for setting border to bar.
        plt.xticks(y_pos, languages)
        plt.xlabel("Lunguages")
        plt.ylabel('Popularity')
        plt.title('Programming language Popularity')
        plt.show()




obj = BarchartTutorial()
# obj.simple_bar_chart()
# obj.horizontal_barchart()
# obj.uniform_color_barchart()
# obj.different_color_barchart()
# obj.text_on_barchart()
obj.blue_border_barchart()