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
    filename1="offensiveDataSet.txt"
    filename2="safeDataSet.txt"
    badData = methods.readFromFile(filename1)
    safeData = methods.readFromFile(filename2)
    safeData = methods.prepareForNLTK(safeData)
    badData = methods.prepareForNLTK(badData)
    safeData = methods.cleanComments(safeData)
    badData = methods.cleanComments(badData)
    methods.writeToFile("cleanSafeComments.txt",safeData)
    methods.writeToFile("cleanBadComments.txt",badData)



#lematizare pt limba romana (dexonline)
#ro-word-net