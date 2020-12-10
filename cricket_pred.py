
# Importing essential libraries
import pandas as pd
import matplotlib.pyplot as plt

# Loading the dataset
df = pd.read_csv('C:/Users/VAMSHI/Desktop/project/deliveries.csv')
df.columns
# --- Data Cleaning ---
# Removing unwanted columns
columns_to_remove = ['match_id', 'is_super_over','player_dismissed','dismissal_kind','fielder']
df.drop(labels=columns_to_remove, axis=1, inplace=True)

# Keeping only consistent teams
consistent_teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
                    'Mumbai Indians', 'Kings XI Punjab', 'Royal Challengers Bangalore',
                    'Delhi Daredevils', 'Sunrisers Hyderabad']
df = df[(df['batting_team'].isin(consistent_teams)) & (df['bowling_team'].isin(consistent_teams))]
df['batsman'].unique()
df.head()
df.columns
df.isna().sum()
# --- Data Preprocessing ---
from sklearn import preprocessing
#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
df['batting_team']=le.fit_transform(df['batting_team'])
df['bowling_team']=le.fit_transform(df['bowling_team'])
df['batsman']=le.fit_transform(df['batsman'])
df['non_striker']=le.fit_transform(df['non_striker'])
df['bowler']=le.fit_transform(df['bowler'])

df.info()

x = df.iloc[:,:15]
y = df.iloc[:,15]

from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.3,random_state = 109) # 70% training and 30% test
#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
gnb = GaussianNB()

#Train the model using the training sets
gnb.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = gnb.predict(X_test)
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

