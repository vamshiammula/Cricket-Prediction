# Cricket-Prediction
In this project I have developed a cricket score predicting using machine learning algorithm here, I took IPL dataset from websites

In cricket_EDA.py code you can see the data visualization part and here what I had done is firstly, i imported data from my desktop and then i did some preprocessing like
imputing missing values and removing unwanted features and plotted graphs using different plots like bar plot, Histogram and Scatter plot.

In cricket_pred.py code you can see the prediction part here i used deliveries.csv file to do the prection and i used naive bayes classifier machine learning algorithm
to get the right results
whey i used this algorithm is navie bayes works on joint and conditional probability so here i have different features in deliveries dataset i know that every feature
will give me some weightage to my output i used this algorithm
before that i did checked for any missing values and if missing values are more than 85% of the data missing then i removed those features and here i kept only consistent teams
and removed unconsistent teams after that i did label encoding to convert categorical values to numerical values then i splitted data into train and test and applied
machine learning algorithm to train the model i trainned my model using training dataset and tested my model using test dataset i got good results

Tools used for project development
1. Python 3.9.0
2. Numpy
3. Pandas
4. matplotlib
5. sklearn
