from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import r2_score
from training.Regression.SupportVectorRegression.Model.PickleGenerator import *
from training.DataManipulation import *

class SupportVectorSalary:

    @staticmethod
    def modelCreationSVR():

        try:
               # To read main csv file and returns train data
               dataSet = pd.read_csv('../Data/Position_Salaries.csv')
               ds = DataController.create_Train_Test_File(dataSet)
               ds = ds[0]

               # Splitting dataset into Traiing set and Testing set
               x_index = ds.columns.get_loc('Level')
               y_index = ds.columns.get_loc('Salary')
               # x_data = ds.iloc[:, 1:2].values
               # y_data = ds.iloc[:, 2:].values
               x_data = ds.iloc[:, [x_index]].values
               y_data = ds.iloc[:, [y_index]].values
               x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=1/3, random_state=0)

               # Feature Scaling
               x_scaler = StandardScaler()
               y_scaler = StandardScaler()
               x_train = x_scaler.fit_transform(x_train)
               x_test = y_scaler.fit_transform(x_test)

               # Fitting SVR to the dataset
               regressor = SVR(kernel='rbf')
               regressor.fit(x_train, y_train)

               # Predicting test result set
               y_predict = regressor.predict(x_test)
               accuracy_train = r2_score(y_test, y_predict)
               print("Accuracy of train data is :", accuracy_train)

               # Set path of test csv file
               test_csv_path = input("Enter test csv path:")

               # To create and save pickle file
               y_test_predict = Pickle_Model.create_save_pickle(test_csv_path, regressor,y_test)


        except Exception as e:
               print(e)


SupportVectorSalary.modelCreationSVR()