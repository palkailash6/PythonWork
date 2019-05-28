#importing the library.
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import collections
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
class NLPDemo:

    def getPositiveNegativeReview(self):

        #importing the dataset.
        dataset = pd.read_csv('Restaurant_Reviews.tsv',delimiter='\t',quoting=3)
        corpus  = []
        # print(dataset)
        #cleaning the dataset
        for i in range(0,1000):
            review = re.sub('[^a-zA-z]',' ',dataset['Review'][i])
            review = review.lower().split()

            # finding the root of word which has same meaning for love word using stem.
            ps = PorterStemmer()
            review = [ps.stem(word) for word in review if not word in stopwords.words('english')] # checking english
            # word like "this" is present in stopword library
            review = ' '.join(review)
            corpus.append(review)

        # create bag of words model.
        cv = CountVectorizer(max_features=1500)
        x = cv.fit_transform(corpus).toarray()

        # getting the dependent variable values i.e liked
        y = dataset.iloc[:, 1].values
        x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.2)

        # feature scalling
        sc_x = StandardScaler()
        sc_y = StandardScaler()
        x_train  = sc_x.fit_transform(x_train)
        x_test  = sc_y.fit_transform(x_test)

        # Fitting Navie Bayes to the trainning set
        from sklearn.naive_bayes import GaussianNB
        classifier = GaussianNB()
        classifier.fit(x_train, y_train)

        # Predicting test set
        y_pred = classifier.predict(x_test)

        #making the confusion matrix.
        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(y_test,y_pred)

        #find accuracy
        accuracy = accuracy_score(y_pred,y_test)
        print("accuracy:",accuracy)



nlp_obj = NLPDemo()
nlp_obj.getPositiveNegativeReview()