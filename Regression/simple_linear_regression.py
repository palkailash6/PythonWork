# @author  Kailash Pal
# @version 1.0
# Simple class for demonstrating the regression models.

# importing the libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Creating class for implementing the regression problem:
class RegressionExample:
    def model_predict_sal_based_exp(self):

        #importing the dataset
        data = pd.read_csv("Salary_Data.csv")
        x_data = data.iloc[:,:-1].values
        print(x_data)
        y_data = data.iloc[:,1].values

        #splitting dataset into trainning and test set.
        x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=15,random_state= 0)

        # Fitting simple linear example to trainning dataset.
        lnr_regrsn = LinearRegression()
        lnr_regrsn.fit(x_train,y_train)
        predicted_val = lnr_regrsn.predict(x_test)
        print("Predicted val is:",predicted_val)

        # Plotting the train data set
        plt.scatter(x_train,y_train,color = 'red')
        plt.plot(x_train,lnr_regrsn.predict(x_train),color = 'yellow')
        plt.title('Salary vs Exp (trainning set)')
        plt.xlabel('Years of Experience')
        plt.ylabel('salary')
        plt.show()

        # Plotting the test data set
        plt.scatter(x_test, y_test, color='blue')
        plt.plot(x_train, lnr_regrsn.predict(x_train), color='green')
        plt.title('Salary vs Exp (Test set)')
        plt.xlabel('Years of Experience')
        plt.ylabel('salary')
        plt.show()



    #Creating function for demonstrating bike shared based on temperature.
    def get_predict_bike_vs_temp(self):

        #importing the dataset
        bike_data = pd.read_csv("bike_sharing.csv")
        bike_df = pd.DataFrame(bike_data)
        x_data = bike_df[['temp']]
        y_data = bike_df[['cnt']]
        print(x_data)
        print(y_data)

        #spliting test and train data
        x_train, x_test,y_train , y_test = train_test_split(x_data,y_data,test_size=100,random_state= 0)

        # fitting in trainning set
        regressor = LinearRegression()
        regressor.fit(x_train,y_train)
        regressor.predict(x_test)

        #visualizing the trainning set
        plt.scatter(x_train,y_train,color ='red')
        plt.plot(x_train,regressor.predict(x_train))
        plt.xlabel("Bike")
        plt.ylabel("Count")
        plt.title("Bike shared on Temp- Training set")
        plt.show( )

        # visualizing the test set
        plt.scatter(x_test, y_test, color='yellow')
        plt.plot(x_train, regressor.predict(x_train))
        plt.xlabel("Bike")
        plt.ylabel("Count")
        plt.title("Bike shared on Temp- Test set")
        plt.show()


# Creating object and calling the fuction
obj = RegressionExample()
obj.model_predict_sal_based_exp()
# obj.get_predict_bike_vs_temp()
