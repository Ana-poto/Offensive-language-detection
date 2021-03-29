import methods

if __name__ == '__main__':

    # # Extract vocabulary from commnents
    # badData=normalization(badData)
    # safeData=normalization(safeData)
    # safeWords=tokenizer(listToString(safeData))
    # print("==========================================")
    # badWords = tokenizer(listToString(badData))
    # print("==========================================")
    # writeToFile("safeWords.txt",safeWords)
    # writeToFile("badWords.txt",badWords)

    # Clean comments
    filename1="E:\GitHub\Offensive-language-detection\DataPreprocessing\InitialDataset\offensiveDataSet.txt"
    filename2="E:\GitHub\Offensive-language-detection\DataPreprocessing\InitialDataset\safeDataSet.txt"
    badData = methods.readFromFile(filename1)
    safeData = methods.readFromFile(filename2)
    # safeData = methods.prepareForNLTK(safeData)
    # badData = methods.prepareForNLTK(badData)
    safeData = methods.cleanComments(safeData)
    badData = methods.cleanComments(badData)
    methods.writeToFile("Comments/cleanSafeComments.txt", safeData)
    methods.writeToFile("Comments/cleanBadComments.txt", badData)



#lematizare pt limba romana (dexonline)
#ro-word-net
#eliminare cuvinte mai mari de 16 caractere