import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
class BarchartTutorial:
    def simple_bar_chart(self):
        languages = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
        print(type(languages))
        y_pos = np.arange(len(languages))
        popularity = [10, 8, 6, 4, 2, 1]

        plt.bar(y_pos, popularity , align='center', alpha=0.5)
        plt.xticks(y_pos, languages)
        plt.xlabel("Lunguages")
        plt.ylabel('Popularity')
        plt.title('Programming language Popularity')

        plt.show()


obj = BarchartTutorial()
obj.simple_bar_chart()