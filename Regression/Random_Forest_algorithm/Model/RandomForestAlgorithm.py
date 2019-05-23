import pandas as pd
from training.DataManipulation import *
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
import pickle

class RandomForestAlgorithm:

    # Importing dataset
    dataSet = pd.read_csv('../Data/Position_Salaries.csv')
    length_old = len(dataSet.columns)

    # Handling categorical data
    positions = pd.get_dummies(dataSet['Position'])
    dataSet = dataSet.drop('Position', axis=1)
    dataSet = pd.concat([dataSet, positions], axis=1)

    # Splitting dataset into 2 different csv files
    train_file = DataController.create_Train_Test_File(dataSet)
    type(train_file)
    train_file = train_file[0]
    print(train_file)
    # df_training = dataSet.sample(frac=0.7)
    # df_test = pd.concat([dataSet, df_training]).drop_duplicates(keep=False)

    # dataSet = pd.read_csv(train_file)

    length_new = len(train_file.columns)

    y_index = train_file.columns.get_loc("Salary")

    y = train_file.iloc[:, y_index:(y_index + 1)]
    x = train_file.iloc[:, (length_old - 1):length_new]

    # Checking for null values
    if y['Salary'].isnull().sum() > 0:
        print("Taking care of null values of Salary column")
        y = y.fillna(y.mean())

    # Feature scaling
    scX = StandardScaler()
    x = scX.fit_transform(x)

    # Splitting data into training and test set
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    # # Fitting training data into model
    regression = RandomForestRegressor(n_estimators=10, random_state=0)
    regression.fit(x_train, y_train.values.ravel())

    # Using model to predict test data
    y_pred = regression.predict(x_test)

    # Calculating accuracy
    accuracy = r2_score(y_test, y_pred)
    print("Accuracy from model is : ", accuracy)

    # Dumping model into pickle
    # if accuracy > 0.8:
    pickle_name = input("mention the name for pickle file : ")
    file_name = '/home/admin1/PycharmProjects/bridgelabz/training/Regression/Random_Forest_algorithm/Data' + "/" + pickle_name + ".pkl"
    pkl_file = open(file_name, 'wb')
    model = pickle.dump(regression, pkl_file)

    # Loading pickle model to predict data from test_data.csv file
    pkl_file = open(file_name, 'rb')
    model_pkl = pickle.load(pkl_file)

    dataSet_testdata = pd.read_csv('/home/admin1/PycharmProjects/bridgelabz/training/Regression/Random_Forest_algorithm/Data/Train.csv')

    x_testdata = dataSet_testdata.iloc[:, (length_old - 1):length_new]
    y_testdata = dataSet_testdata.iloc[:, y_index:(y_index + 1)]

    y_pred_pkl = model_pkl.predict(x_testdata)

    # Calculating accuracy from pickle model
    accuracy_pk = r2_score(y_testdata, y_pred_pkl)
    print("Accuracy by pickle model ", accuracy_pk)




