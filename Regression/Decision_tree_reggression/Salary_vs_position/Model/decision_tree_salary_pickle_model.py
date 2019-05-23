import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor


from training.Regression.Regression_Test_Algorithm import *
from training.Regression.Regression_Train_Algorithm import *
class ControllerDecisionSalary:

    def model_creation_decision_salary(self):
        simple = RegressionModelPreparation()
        file = simple.csv_frm_input()
        dataset = simple.get_train_test_csv_file(file)
        train_csv_path = simple._datapreprocessing(dataset)

        train_data = pd.read_csv(train_csv_path)
        # train_data = dataset[0]

        #getting column value from dataset.
        df = pd.DataFrame(train_data)
        column_x = input("Enter X - Column name :")
        x_val = df[[column_x]].values
        column_y = input("Enter Y - Column name :")
        y_val = df[[column_y]].values


        #spliting in test train data.
        values  = RegressionModelPreparation().get_test_train_split_data(x_val,y_val)

        # Fitting training set
        regression = DecisionTreeRegressor(random_state=0)
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

        # Train data plotting
        obj.decision_plotting(values, "Train_Plot", regression, "Salary vs Position train plot", "Level","Salary")

        test_obj = Test_data_Regression()
        accuracy_pkl_test = test_obj.get_test_accuraccy()
        print("Accuracy of test data:", accuracy_pkl_test)

        # Train data plotting
        obj.decision_plotting(values, "Test_Plot", regression, "Salary vs Position test plot", "Level","Salary")

    def decision_plotting(self, values, plot_type, model, title, xlabel_val, ylabel_val):
        if plot_type == "Train_Plot":
            x_val = values.x_train
            y_val = values.y_train
        else:
            x_val = values.x_test
            y_val = values.y_test

        X_grid = np.arange(min(x_val), max(x_val), 0.1)

        X_grid = X_grid.reshape((len(X_grid), 1))

        # scatter plot for original data
        plt.scatter(x_val, y_val, color='red')

        # plot predicted data
        plt.plot(X_grid, model.predict(X_grid), color='blue')

        # specify title
        plt.title(title)

        # specify X axis label
        plt.xlabel(xlabel_val)

        # specify Y axis label
        plt.ylabel(ylabel_val)

        # show the plot
        plt.show()

obj = ControllerDecisionSalary()
obj.model_creation_decision_salary()