import pandas as pd
import numpy as np
class PandasTutorial:
    def one_dimenson_wth_pandas(self):
        ds = pd.Series([2, 4, 6, 8, 10],dtype=int)
        print(ds)

    def convert_series_list(self):
        ds = pd.Series(input("Enter series:"))
        print("Series are:",ds,"\n Type of series is:",type(ds))
        print("Converting series to list:",ds.tolist())
        print("Type of list is:",type(ds.tolist()))

    def calculation_on_series(self):

        data_series1 = pd.Series([2, 4, 6, 8, 10])
        data_series2 = pd.Series([1, 3, 5, 4, 8])
        ds_add = data_series1 + data_series2
        print("Addition of two series:")
        print(ds_add)

        ds_add = data_series1 - data_series2
        print("Substaction of two series:", ds_add)

        ds_add = data_series1 * data_series2
        print("Multiplication of two series:", ds_add)

        ds_add = data_series1 / data_series2
        print("Substaction of two series:", ds_add)

    def power_of_aaray_element_wise(self):
        value1 = np.array([1,5,6,9,8,2])
        value2 = np.array([1,3,3,3,3,2])

        print("Power of array elements are:" ,np.power(value1,value2))
        print("Power of array based on 3 are:" ,np.power(value1,3))

    def data_frame(self):
        exam_data = {
            'name': ['kailash', 'vani', 'vinay','Dhiraj'],
            'score': [12.5, 9, 16.5, np.nan],
            'attempts': [1, 3, 2, 3],
            'qualify': ['yes', 'no', 'yes', 'no']}
        labels = [1,2,3,4]

        df = pd.DataFrame(exam_data, index=labels)
        print(df)
        return df

    def summary_data_frame(self):
        exam_data = {
            'name': ['kailash', 'vani', 'vinay', 'Dhiraj'],
            'score': [12.5, 9, 16.5, np.nan],
            'attempts': [1, 3, 2, 3],
            'qualification': ['B.com', 'BMS', 'BE', 'Under graduate']}
        labels = [1, 2, 3, 4]

        df = pd.DataFrame(exam_data, index=labels)
        print(df.info())

    def get_rows_frm_data_frame(self):
        df = obj.data_frame()
        print("After slicing:")
        print(df.iloc[0:3])

    def get_column_name(self):
        df = obj.data_frame()
        print("\n Printing only name and score column's data :")
        print(df[['name', 'score']])


    def get_rows_column_name(self):
        df = obj.data_frame()
        print("\n Select specific columns and rows:")
        print(df.iloc[[1, 3], [1, 3]])

    def get_no_attempts(self):
        df = obj.data_frame()
        print("Rows where attempts greater than 2 :")
        print(df[df['attempts'] > 2])

    def get_rows_col_count_df(self):
        df = obj.data_frame()
        total_rows = len(df.axes[0])
        total_cols = len(df.axes[1])
        # print("Row value: ",df.axes[0])
        # print("Col value: ",df.axes[1])
        print("\nNumber of Rows: " ,total_rows)
        print("Number of Columns: " ,total_cols)

obj = PandasTutorial()
# obj.one_dimenson_wth_pandas()
# obj.convert_series_list()
# obj.calculation_on_series()
# obj.power_of_aaray_element_wise()
# obj.data_frame()
# obj.summary_data_frame()
# obj.get_rows_frm_data_frame()
# obj.get_column_name()
# obj.get_rows_column_name()
# obj.get_no_attempts()
obj.get_rows_col_count_df()