from training.Regression.Regression_Train_Algorithm import *
from sklearn.metrics import r2_score
import pandas as pd
import pickle


class Test_data_Regression (pickle_generator):

    def load_pickle_model(self):
        # obj_pickle = pickle_generator()
        pickle_file_dir = input("Provide the directory path to Read pickle file : ")
        pickle_file_name = input("Name of Pickel file to read: ")
        pickle_file_path = pickle_file_dir + "/" + pickle_file_name + ".pkl"
        pkl_read = pickle_generator().readPickleFile(pickle_file_path)
        return pkl_read

    # def load_pickle_encoder(self):
    #     # obj_pickle1 =pickle_generator()
    #     pkl_encode_read = pickle_generator().readPickleFile('/home/admin1/PycharmProjects/bridgelabz/training/Regression/Linear_Reggression/salary/Data/Linear_salary_encoder.pkl')
    #     return pkl_encode_read

    def get_test_accuraccy(self):
        # obj.load_pickle_encoder()
        linear_model = obj.load_pickle_model()

        #read csv
        dataset = pd.read_csv('../Data/Test.csv')
        # dataset = pd.read_csv('/home/admin1/PycharmProjects/bridgelabz/training/Regression/Linear_Reggression/salary/Data/Test.csv')

        #get column value
        df = pd.DataFrame(dataset)
        column_x = input("Enter X - Column name :")
        x_val = df[[column_x]]
        column_y = input("Enter Y - Column name :")
        y_val = df[[column_y]]

        # x_val = df[['YearsExperience']]
        # y_val = df[['Salary']]


        # Use pickle's regression model to Predict y values and calculate Accuracy
        y_pred_pkl = linear_model.predict(x_val)

        accuracy_pkl = r2_score(y_pred_pkl, y_val)
        return accuracy_pkl


obj = Test_data_Regression()
