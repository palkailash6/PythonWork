# @author  Kailash Pal
# @version 1.0
# Simple class for demonstrating the regression models.

# importing the libraries.
# importing Libraries
# importing Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle


class Simple_Regression:

    try:

        def simple_regression_using_pickle(self):

            # Importing data-set and converting into two csv Files

            csv_dataset = pd.read_csv('Salary_Data.csv')
            data_train = csv_dataset.sample(frac=0.8)
            data_test = pd.concat([csv_dataset, data_train]).drop_duplicates(keep=False)

            data_train.to_csv('train_file.csv', header=True, index = None)
            data_test.to_csv('test_file.csv', header=True, index = None)

            dataset = pd.read_csv('train_file.csv')

            # Find col index using columns and get_loc fun
            """columns retuen all col of given dataset and 
            get_loc fun return the specified index of col"""

            x_index = dataset.columns.get_loc("YearsExperience")
            y_index = dataset.columns.get_loc("Salary")

            x = dataset.iloc[:, x_index:(x_index+1)]
            y = dataset.iloc[:, y_index:(y_index+1)]

            # Checking for null values
            if dataset['Salary'].isnull().sum() > 0:
                print("Taking care of null values of salary column")
                x = x.fillna(x.mean())

            if dataset['YearsExperience'].isnull().sum() > 0:
                print("Taking care of null values of exp column")
                y = y.fillna(y.mean())

            else:
                print("Null values are not present")

            # Splitting data-set into training and test set
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

            # Fitting training set
            regression = LinearRegression()
            regression.fit(x_train, y_train)

            # Predicting test set
            y_pred = regression.predict(x_test)

            # Calculating accuracy of model
            accuracy = r2_score(y_test, y_pred)
            print("Accuracy of Model : ", accuracy)

            # Creating and saving pickle model
            pkl_file_name_path = 'Linear_Regression.pkl'
            linear_regression_model = open(pkl_file_name_path, 'wb')
            pickle.dump(regression, linear_regression_model)
            linear_regression_model.close()

            # Loading pickle model to predict y data from test_data.csv
            linear_regression_model = open(pkl_file_name_path, 'rb')
            regression_model_pkl = pickle.load(linear_regression_model)

            """Spliting Test Dataset into Train and Test for calculate Accuracy of Test Dataset"""

            ds_testData = pd.read_csv('test_file.csv')
            x_test_Data = ds_testData.iloc[:, x_index:(x_index + 1)]
            y_test_Data = ds_testData.iloc[:, y_index:(y_index + 1)]

            # Use pickle's regression model to Predict y values and calculate Accuracy
            y_pred_pkl = regression_model_pkl.predict(x_test_Data)

            accuracy_pkl = r2_score(y_pred_pkl, y_test_Data)
            print("Accuracy of test data using Pickle File: ", accuracy_pkl)

    except:
        print("Exception")


obj = Simple_Regression()
obj.simple_regression_using_pickle()