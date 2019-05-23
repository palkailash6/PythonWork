import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


from training.Regression.Regression_Test_Algorithm import *
from training.Regression.Regression_Train_Algorithm import *
class Controller:

    def model_creation(self):
        simple = RegressionModelPreparation()
        file = simple.csv_frm_input()
        dataset = simple.get_train_test_csv_file(file)
        train_csv_path = simple._datapreprocessing(dataset)

        train_data = pd.read_csv(train_csv_path)
        # train_data = dataset[0]

        #getting column value from dataset.
        df = pd.DataFrame(train_data)
        column_x = input("Enter X - Column name :")
        x_val = df[[column_x]]
        column_y = input("Enter Y - Column name :")
        y_val = df[[column_y]]
        # x_val = df[['temp']].values
        # y_val = df[['cnt']].values

        #pre-processing step.
        if train_data[column_x].isnull().sum() > 0:
            x_val = x_val.fillna(x_val.mean())

        if train_data[column_y].isnull().sum() > 0:
            y_val = y_val.fillna(y_val.mean())

        #spliting in test train data.
        values  = RegressionModelPreparation().get_test_train_split_data(x_val,y_val)

        # Fitting training set
        regression = LinearRegression()
        regression.fit(values.x_train, values.y_train)

        # Predicting test set
        y_pred = regression.predict(values.x_test)

        # get accuracy
        accuracy_pkl = r2_score(values.y_test, y_pred)
        print("Accuracy of train data model: ", accuracy_pkl)


        pickle_file_dir = input("Provide the directory path to save pickle file : ")
        pickle_file_path = input("Enter the Name of pickle file to be saved: ")
        pickle_file = pickle_file_dir + "/" + pickle_file_path + ".pkl"
        #pickle creator.
        obj_pikal = pickle_generator().writePickleFile(regression,pickle_file)



        # Plotting train set results
        simple.graph_plotting(regression,values.x_train, values.y_train,"Train data plot","Temprature","Bike")
        test_obj = Test_data_Regression()
        test_linear_pkl_model = test_obj.get_test_accuraccy()

        # Test model prediction
        simple.graph_plotting(regression, values.x_test, values.y_test,"Test data plot","Temprature","Bike")


obj = Controller()
obj.model_creation()