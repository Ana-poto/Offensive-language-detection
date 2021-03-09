import re
from nltk.corpus import stopwords, brown
from nltk.tokenize import word_tokenize
import spacy
import ro_core_news_sm

def readFromFile(filename):
    data = list()
    lineList = list()
    with open(filename,"r+", encoding="utf-8") as f:
        lineList = f.readlines()
        for line in lineList:
            data.append(line)
    return removeEmptyLines(data)

def writeToFile(filename,inputData):
    with open(filename,"w+", encoding="utf-8") as f:
        for word in inputData:
            f.write(word)
            f.write("\n")
    f.close()
    print("Done")
    return None

def listToString(inputData):
    resultString = str()
    for s in inputData:
        resultString+=str(s)+" "
    return resultString

def removeEmptyLines(inputData):
    return [x.strip() for x in inputData if x.strip()]


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
    words = [word for word in tokens if word.isalpha()]
    print("Words ", len(words))
    #remove all english words
    englishWords =  set(w.lower() for w in brown.words())
    result = [w for w in words if not w in englishWords]
    #remove stopwords
    stop_words = set(stopwords.words('romanian'))
    finalWords = [w for w in result if not w in stop_words]
    print("Items ", len(finalWords))
    return finalWords

def normalization(inputData):
    spacy.prefer_gpu()
    nlp = spacy.load("ro_core_news_sm")
    return nlp(inputData)

if __name__ == '__main__':
    filename1="offensiveDataSet.txt"
    filename2="safeDataSet.txt"
    badData = readFromFile(filename1)
    safeData = readFromFile(filename2)
    safeData=str(listToString(prepareForNLTK(safeData)))
    badData=str(listToString(prepareForNLTK(badData)))

    badData=normalization(badData)
    safeData=normalization(safeData)
    safeWords=tokenizer(listToString(safeData))
    print("==========================================")
    badWords = tokenizer(listToString(badData))
    print("==========================================")
    writeToFile("safeWords.txt",safeWords)
    writeToFile("badWords.txt",badWords)
