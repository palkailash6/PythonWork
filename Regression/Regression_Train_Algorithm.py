# @author  Kailash Pal
# @version 1.0
# Simple class for demonstrating the regression models.

# importing the libraries.

from sklearn.preprocessing import StandardScaler
from training.DecisionTree import *
import os
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

# Used for pickle file creation and loading.
class pickle_generator():
    @staticmethod
    def writePickleFile(model_name,pkl_file_name):
        pikle_file= open(pkl_file_name,'wb')
        pickle.dump(model_name,pikle_file)
        pikle_file.close()

    @staticmethod
    def readPickleFile(pkl_file_name):
        pikle_file = open(pkl_file_name, 'rb')
        model_pkl = pickle.load(pikle_file)
        return model_pkl


# Used for algorithm creation
class RegressionModelPreparation:

    @staticmethod
    def user_input():
        userInput = input("Enter File Path: ")  # Take User Input as file path
        if not userInput.endswith('.csv'):  # Check file Extention is .csv
            raise ValueError("File format invalid")
        if not os.path.isfile(userInput):
            raise FileNotFoundError("File does not exist at path:")
        return userInput

    @staticmethod
    def get_column_index_number(data_set,column_name):
        col_index = data_set.columns.get_loc(column_name)
        return col_index

    @staticmethod
    def create_csv_file(data_set,csv_path):
        data_set.to_csv(csv_path, header=True, index=None)
    @staticmethod
    def read_csv_file(csv_path):
        dataset = pd.read_csv(csv_path)
        return dataset

    def get_train_test_csv_file(self,csv_file):
        data_train = csv_file.sample(frac=0.8)
        data_test = pd.concat([csv_file, data_train]).drop_duplicates(keep=False)
        train_test_dir = input("Provide the directory path to save file : ")
        train_file = input("enter the train file name : ")
        test_file = input("enter the test file name : ")
        train_csv_path = train_test_dir + "/" + train_file + ".csv"
        test_csv_path = train_test_dir + "/" + test_file + ".csv"

        if not os.path.exists(train_test_dir):
            os.makedirs(train_test_dir)
            if not os.path.isfile(train_csv_path):
                data_train.to_csv(train_csv_path, header=True, index=None)

            if not os.path.isfile(test_csv_path):
                data_test.to_csv(test_csv_path, header=True, index=None)
        else:
            if not os.path.isfile(train_csv_path):
                data_train.to_csv(train_csv_path, header=True, index=None)

            if not os.path.isfile(test_csv_path):
                data_test.to_csv(test_csv_path, header=True, index=None)

        return train_csv_path
        # #preproccessing steps
        # train_csv_path = obj._datapreprocessing(train_csv_path)
        #
        #
        # df_train = pd.read_csv(train_csv_path)
        # # print("data_train {} ,datatest {}".format(data_train,data_test))
        # return df_train,data_test


    def csv_frm_input(self):
        csv_file =  input("Enter the path of csv file:")
        try:
            csv_dataset = pd.read_csv(csv_file)
            return csv_dataset
        # /home/admin1/PycharmProjects/bridgelabz/training/Regression/Linear_Reggression/salary/Data/Salary_Data.csv
        except:
            print("Exception of csv path")

    def pre_ProcessingSteps(data_set,column_name,x_val,y_val):
        if data_set[column_name].isnull().sum() > 0:
            print("Taking care of null values of salary column")
            x_val = x_val.fillna(x_val.mean())

    def labelEncoding(self,column_value):
        # Encoding the Independent Variable
        from sklearn.preprocessing import LabelEncoder
        label_encoder = LabelEncoder()
        column_value = label_encoder.fit_transform(column_value)
        return column_value,label_encoder

    @staticmethod
    def feature_scale(column):
        # Feature scaling
        scX = StandardScaler()
        x_val = scX.fit_transform(column)
        return x_val

    @staticmethod
    def get_test_train_split_data(x_val,y_val):
        from sklearn.model_selection import train_test_split
        import collections

        # Declaring namedtuple()
        train_test_data = collections.namedtuple('train_test_data', ['x_train', 'x_test', 'y_train', 'y_test'])
        value = train_test_split(x_val, y_val, test_size=0.2)
        return train_test_data(*value)

    def graph_plotting(self,model,x_val,y_val,title,x_label,y_label):
        plt.scatter(x_val, y_val, color='red')
        plt.plot(x_val, model.predict(x_val), color='blue')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()

    def _datapreprocessing(self, csv_file_path):
        """""
        :return: Clean Data set after applying necessary pre-processing steps on data
        """
        """
        imputation fills in the missing value with some number. 
        The imputed value won't be exactly right in most cases, 
        but it usually gives more accurate models than dropping the column entirely.     
        The default behavior fills in the mean value for imputation.
        """
        missing_values = ["n/a", "na", "-"]
        df = pd.read_csv(csv_file_path, na_values=missing_values)
        # Check For missing Data and null

        # df = pd.read_csv("/home/admin1/PycharmProjects/Demo/PythonPackages/PlotPath/Position_Salaries.csv")
        if df.isnull().sum().sum() > 0:
            df_1 = pd.DataFrame((df).astype('category'))
            imp = SimpleImputer(strategy="most_frequent")
            imp = imp.fit_transform(df_1)
            new_dataframe = pd.DataFrame(imp)
        else:

            new_dataframe = df

        # check if any categorical data present
        # objregression._estimator_type
        cat_col = df.select_dtypes(include=['object']).columns
        if cat_col.dtype.name == 'object':
            categorical_index = [df.columns.get_loc(c) for c in cat_col if c in df]
            encoder_df = new_dataframe.iloc[:, categorical_index]
            onehotencoder = OneHotEncoder()
            for iteindex in categorical_index:
                onehotencoder.fit(encoder_df)
                onehotlabels = onehotencoder.transform(encoder_df).toarray()
                converteddata = pd.DataFrame(onehotlabels)
                ds = new_dataframe.drop(cat_col, axis=1)
                df = pd.concat([ds, converteddata], axis=1)

            file_name = input("Provide the path of train csv including csv file: ")
            # file_name = "/home/admin1/PycharmProjects/bridgelabz/training/Regression/Linear_Reggression/salary/Data/Train.csv"
            df.to_csv(file_name, header=True, index=None)
            return file_name
        else:
            return csv_file_path




obj = RegressionModelPreparation()