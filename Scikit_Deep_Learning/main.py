import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import seaborn as sb
# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.metrics import classification_report

# --------------------------Data Collections and Preprocessing-----------------------
# Import of data
df = pd.read_csv('/Users/jacobvillegas/Documents/UTD/NLP/last-few/sklearn/Suicide_Detection.csv', header=0, usecols=[1,2], encoding='latin-1')
print('rows and columns:', df.shape)
print(df.head())
# Need to change the column name from class to label due to class is reserved in python
df.rename(columns={"class":"label"}, inplace = True)
data = df[['text', 'label']]
print(data.head())
# print(data.isnull().values.any(), "\n")
# since there is only  two categories "Suicide/ non-suicide, used an ordinal encoder gives binary labeling
ord_encod = OrdinalEncoder()
ord_encod.fit(data[['label']])
data['encoded_label'] = ord_encod.transform(df[["label"]])
data["tweet_length"] = data['text'].str.len()
print(data.shape, list(data.columns))
print(data.head())

# ---plot of data--------
X = data.text
y = data.encoded_label
data_y = pd.DataFrame(y, columns=['encoded_label'])
print(data.shape, list(data.columns))
sb.countplot(x="label", data=data,)
sb.catplot(data = data, x= 'tweet_length', y="label",  )

plt.show()

# ------------------------------Training and Fit--------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, train_size=0.8)

stopwords = set(stopwords.words('english'))
tf_vectorizer = TfidfVectorizer(stop_words='english')
X_train = tf_vectorizer.fit_transform(X_train)
X_test = tf_vectorizer.transform(X_test)


# Naives Bayes
naives_bayes = MultinomialNB()
naives_bayes.fit(X_train, y_train)
predictions = naives_bayes.predict(X_test)
print(confusion_matrix(y_test, predictions))
print("Naives-Bay Report:\n")
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))




# Logistic Regression
logistic_regression = LogisticRegression(solver='lbfgs', class_weight='balanced', max_iter=100)
logistic_regression.fit(X_train, y_train)
predictions = logistic_regression.predict(X_test)
print("Logistic Regression Report:\n")
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))


# Neural Network Classifier
neural_net = MLPClassifier(solver='lbfgs', alpha=1e-5,
                   hidden_layer_sizes=(12, 2), random_state=1, early_stopping=True)
neural_net.fit(X_train, y_train)
predictions = logistic_regression.predict(X_test)
print("Neuarl Network Classifier:\n")
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))







