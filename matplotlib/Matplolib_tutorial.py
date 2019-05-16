import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
class MatPlotDemo:
    def ploting_line(self):
        x_axis = np.array(input("Enter X Co-ordinate value:").split(","),dtype=int)
        y_axis = np.array(input("Enter Y Co-ordinate value:").split(","),dtype=int)
        # Plot lines and/or markers to the Axes.
        plt.plot(x_axis, y_axis)
        plt.show()

    def ploting_with_title(self):
        x_axis = np.array(input("Enter X Co-ordinate value:").split(","), dtype=int)
        y_axis = np.array(input("Enter Y Co-ordinate value:").split(","), dtype=int)
        # Plot lines and/or markers to the Axes.
        plt.xlabel("x-axis")
        plt.ylabel("x-axis")
        plt.title("Draw a line")
        plt.plot(x_axis, y_axis)
        plt.show()

    def line_draw_inpt_frm_txt(self):
        with open("input.txt") as file:
            data = file.read()
        data = data.split('\n')
        x = [(row.split(' ')[0]) for row in data]
        y = [row.split(' ')[1] for row in data]
        x = np.array(x,dtype= int)
        y = np.array(y,dtype= int)
        print("x and y",x,"   ",y)
        plt.plot(x, y)
        # Set the x axis label of the current axis.
        plt.xlabel('x - axis')
        # Set the y axis label of the current axis.
        plt.ylabel('y - axis')
        # Set a title
        plt.title('Sample graph!')
        # Display a figure.
        plt.show()

    def get_line_charts(self):
        df = pd.read_csv('file_data.csv', sep=',', parse_dates=True, index_col=0)
        df.plot()
        plt.show()

    def draw_line_on_same_plot(self):
        # line 1 points
        x1 = [10, 20, 30]
        y1 = [20, 40, 10]
        # plotting the line 1 points
        plt.plot(x1, y1, label="line 1")
        # line 2 points
        x2 = [10, 20, 30]
        y2 = [40, 10, 30]
        # plotting the line 2 points
        plt.plot(x2, y2, label="line 2")
        plt.xlabel('x - axis')
        # Set the y axis label of the current axis.
        plt.ylabel('y - axis')
        # Set a title of the current axes.
        plt.title('Two or more lines on same plot with suitable legends ')
        # show a legend on the plot
        plt.legend()
        # Display a figure.
        plt.show()

    def draw_line_diff_width_color(self):
        # line 1 points
        x1 = [10, 20, 30]
        y1 = [20, 40, 10]
        # line 2 points
        x2 = [10, 20, 30]
        y2 = [40, 10, 30]
        # Set the x axis label of the current axis.
        plt.xlabel('x - axis')
        # Set the y axis label of the current axis.
        plt.ylabel('y - axis')
        # Set a title
        plt.title('Two or more lines with different widths and colors with suitable legends ')
        # Display the figure.
        plt.plot(x1, y1, color='blue', linewidth=3, label='line1-width-3')
        plt.plot(x2, y2, color='red', linewidth=5, label='line2-width-5')
        # show a legend on the plot
        # plt.legend()
        plt.show()

    def plot_line_diff_style(self):
        # line 1 points
        x1 = [10, 20, 30]
        y1 = [20, 40, 10]
        # line 2 points
        x2 = [10, 20, 30]
        y2 = [40, 10, 30]
        # Set the x axis label of the current axis.
        plt.xlabel('x - axis')
        # Set the y axis label of the current axis.
        plt.ylabel('y - axis')
        # Plot lines and/or markers to the Axes.
        plt.plot(x1, y1, color='blue', linewidth=3, label='line1-dotted', linestyle='dotted')
        plt.plot(x2, y2, color='red', linewidth=5, label='line2-dashed', linestyle='dashed')
        # Set a title
        plt.title("Plot with two or more lines with different styles")
        # show a legend on the plot
        plt.legend()
        # function to show the plot
        plt.show()


obj = MatPlotDemo()
# obj.ploting_line()
# obj.ploting_with_title()
# obj.line_draw_inpt_frm_txt()
# obj.get_line_charts()
# obj.draw_line_on_same_plot()
# obj.draw_line_diff_width_color()
obj.plot_line_diff_style()