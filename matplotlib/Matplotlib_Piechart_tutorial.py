import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
class MatPlotPieChartDemo:
    def simple_piechart(self):
        languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
        popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
        # explode 1st slice
        explode = (0, 0.9, 0, 0, 0, 0.9)
        # Plot
        plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=360)

        plt.axis('equal')
        plt.show()


    def piechart_with_title(self):
        languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
        popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
        # explode 1st slice
        explode = (0, 0.9, 0, 0, 0, 0.9)
        # Plot
        plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=360)

        plt.axis('equal')
        plt.title("PopularitY of Programming Language",bbox={'facecolor': '0.8', 'pad': 5})
        plt.show()

    def get_piechart_with_csv(self):
        data = pd.read_csv("medal.csv")
        country_data = data["country"]
        medal_data = data["gold_medal"]
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
        explode = (0.1, 0, 0, 0, 0)
        plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title("Gold medal achievements of five most successful\n" + "countries in 2016 Summer Olympics")
        plt.show()


obj = MatPlotPieChartDemo()
# obj.simple_piechart()
# obj.piechart_with_title()
obj.get_piechart_with_csv()