import re
from nltk.corpus import stopwords, brown
from nltk.tokenize import word_tokenize
import spacy

def readFromFile(filename):
    data = list()
    lineList = list()
    with open(filename,"r+", encoding="utf-8") as f:
        lineList = f.readlines()
        for line in lineList:
            data.append(line)
            data.append("\n")

    return data

def writeToFile(filename,inputData):
    with open(filename,"w+", encoding="utf-8") as f:
        for word in inputData:
            f.write(str(word))
            f.write("\n")
    f.close()
    print("Done")
    return None

def listToString(inputData):
    resultString = str()
    for s in inputData:
        resultString+=str(s)+" "
    return resultString




def prepareForNLTK(inputData):
    result = list()
    preparedData = list()
    for i in inputData:
        result.append(i.lower())
    for i in result:
        preparedData.append(re.sub('\d','', i))
    return list(dict.fromkeys(preparedData))


def tokenizer(inputData):
    #tokens

    tokens = word_tokenize(inputData)
    print("Tokens ", len(tokens))
    #remove all tokens that are not alphabetic
    words = [word.lower() for word in tokens if word.isalpha()]
    print("Words ", len(words))
    #remove all english words
    englishWords =  set(w.lower() for w in brown.words())
    result = [w for w in words if not w in englishWords]
    #remove stopwords
    stop_words = set(stopwords.words('romanian'))
    finalWords = [w for w in result if not w in stop_words and w != "annotation" and len(w) >3 and len(w)<16]
    print("Items ", len(list(dict.fromkeys(finalWords))))
    return list(dict.fromkeys(finalWords))

def cleanComments(inputData):
    #remove all tokens that are not alphabetic
    #remove all english words
    result = list()
    englishWords = set(w for w in brown.words())
    englishWords2 = set(w.capitalize() for w in brown.words())
    lower_englishWords = set(w.lower() for w in brown.words())
    english_stop_words = set(stopwords.words('english'))
    for comment in inputData:
        tokens = word_tokenize(comment)
        comm = str()
        for word in tokens:
            if word not in englishWords and word not in englishWords2 and word not in lower_englishWords or word == "ANNOTATION" :
                if len(word) < 16 and word not in english_stop_words:
                    if word.isalpha():
                        comm+=word+" "
        result.append(comm)
    return result


def normalization(inputData):
    data = list(dict.fromkeys(inputData))
    spacy.prefer_gpu()
    nlp = spacy.load("ro_core_news_sm")
    result=list()
    for s in data:
        result.append(nlp(s))
    return result


def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+")
    return regrex_pattern.sub(r'',text)