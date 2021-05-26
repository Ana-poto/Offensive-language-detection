"""
Reference : see vocabulary extraction for Phase_2_DataPreprocessing
"""
from nltk import word_tokenize
from nltk.corpus import stopwords

from Phase_2_DataPreprocessing import methods
from sklearn.feature_extraction.text import TfidfVectorizer

def annotation_neutral_words(inputData):
    #tokens
    words_dict = dict.fromkeys(inputData)
    stop_words = set(stopwords.words('romanian'))
    for i in range(len(inputData)):
        if inputData[i] in stop_words:
            words_dict.update({inputData[i],'neutru'})
    print(words_dict)
def tif_vec(text):
    # create the transform
    vectorizer = TfidfVectorizer()
    # tokenize and build vocab
    vectorizer.fit(text)
    # summarize
    print(vectorizer.vocabulary_)
    print(vectorizer.idf_)
    # encode document
    vector = vectorizer.transform([text[0]])
    # summarize encoded vector
    print(vector.shape)
    print(vector.toarray())

if __name__ == '__main__':
    data = methods.readFromFile("/Phase_2_DataPreprocessing\Vocabulary\words.txt")
    annotation_neutral_words(data)
    datatext = methods.readFromFile("E:\GitHub\Offensive-language-detection\DataColector\ColectingPhase2\commentsWithourLabel.txt")
    tif_vec(datatext)