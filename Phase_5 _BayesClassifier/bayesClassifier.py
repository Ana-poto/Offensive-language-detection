
# load the iris dataset
import ast

from sklearn.datasets import load_iris
iris = load_iris()

# store the feature matrix (X) and response vector (y)
X = iris.data
y = iris.target

# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

# training the model on training set
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# making predictions on the testing set
y_pred = gnb.predict(X_test)

# comparing actual response values (y_test) with predicted response values (y_pred)
from sklearn import metrics
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)
def getProbabilities(filename):
    dictionary = {}
    with open(filename, mode='r', encoding='UTF-8', errors='strict', buffering=1) as file:
        for line in file:
            key, value = line.split()
            dictionary[key] = value
    return dictionary

def getBayesScores(data):
    score=0
    probs = getProbabilities("voc.txt")
    print(probs)
    for el in data.split("\\s+"):
        word = el[1:].replace('"',"")
        if word in probs.keys():
            score = score + probs.get(word)
    return score

def getLabel(data):
    label = ['pozitiv', 'neutru' , 'offensator']
    labelPoints = getBayesScores(data)
    print(labelPoints)
    if labelPoints < 0.3:
        return label[1]
    elif labelPoints >= 0.2:
        return label[0]
    else:
        return label[2]