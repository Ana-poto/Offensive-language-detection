# TfidfVectorizer
# CountVectorizer
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
import pandas as pd
def readFromFile(filename):
    data = list()
    lineList = list()
    with open(filename,"r+", encoding="utf-8") as f:
        lineList = f.readlines()
        for line in lineList:
            data.append(line)
            data.append("\n")

    return numpy.array(data)
# set of documents
data = readFromFile("E:\GitHub\Offensive-language-detection\DataAnnotation\RawCommentsForAnnotations\RawDataset1.txt")
train = data
test = ['Arta suporta foarte multe cinismul nu exista arta batiicampii zicand asta']
# instantiate the vectorizer object
countvectorizer = CountVectorizer(analyzer= 'word', stop_words='english')
tfidfvectorizer = TfidfVectorizer(analyzer='word',stop_words= 'english')
# convert th documents into a matrix
count_wm = countvectorizer.fit_transform(train)
tfidf_wm = tfidfvectorizer.fit_transform(train)
#retrieve the terms found in the corpora
# if we take same parameters on both Classes(CountVectorizer and TfidfVectorizer) , it will give same output of get_feature_names() methods)
#count_tokens = tfidfvectorizer.get_feature_names() # no difference
count_tokens = countvectorizer.get_feature_names()
tfidf_tokens = tfidfvectorizer.get_feature_names()
df_countvect = pd.DataFrame(data = count_wm.toarray(),index = ['Doc1','Doc2'],columns = count_tokens)
df_tfidfvect = pd.DataFrame(data = tfidf_wm.toarray(),index = ['Doc1','Doc2'],columns = tfidf_tokens)
print("Count Vectorizer\n")
print(df_countvect)
print("\nTD-IDF Vectorizer\n")
print(df_tfidfvect)