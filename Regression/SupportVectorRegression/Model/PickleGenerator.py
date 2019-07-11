import pickle
import pandas as pd
from sklearn.metrics import r2_score

class Pickle_Model:

        @staticmethod
        def create_save_pickle(testcsv, regression_model,y_test):
            """
            :param testcsv:Path to save test csv file
            :param regression_model:Stores regression model data
            :return:None
            """

            support_vector_pkl_filename = '/home/admin1/PycharmProjects/bridgelabz/training/Regression/SupportVectorRegression/Data/support_vector.pkl'

            # Write and save file in pkl format
            support_vector_model_pkl = open(support_vector_pkl_filename, 'wb')
            pickle.dump(regression_model, support_vector_model_pkl)

            # Close the pickle instance
            support_vector_model_pkl.close()

            # Loading the saved decision tree model pickle
            decision_tree_model_pkl = open(support_vector_pkl_filename, 'rb')
            pickel_model = pickle.load(decision_tree_model_pkl)

            # Read test csv file
            df = pd.read_csv(testcsv)
            X_test = df.iloc[:, [1]].values

            # To predict output based on pickel model
            y_pred = pickel_model.predict(X_test)
            accuracy_test = r2_score(y_test, y_pred)
            print("Accuracy of test data is :", accuracy_test)