import methods

if __name__ == '__main__':

    # # Read from files
    # filename1 = "CleanComments/cleanBadComments.txt"
    # filename2 = "CleanComments/cleanSafeComments.txt"
    # # Extract vocabulary from commnents
    # badData = methods.readFromFile(filename1)
    # badData = methods.normalization(badData)
    # badWords = methods.tokenizer(methods.listToString(badData))
    # methods.writeToFile("Vocabulary/badWords.txt",badWords)
    # print("==========================================")
    #
    #
    # safeData = methods.readFromFile(filename2)
    # safeData=methods.normalization(safeData)
    # safeWords=methods.tokenizer(methods.listToString(safeData))
    # methods.writeToFile("Vocabulary/safeWords.txt", safeWords)
    # print("===========================================")
    # Read from files
    filename = "../DataColector/ColectingPhase2/allComments.txt"
    # Extract vocabulary from commnents
    rawData = methods.readFromFile(filename)
    Data = methods.normalization(rawData)
    Words = methods.tokenizer(methods.listToString(Data))
    methods.writeToFile("Vocabulary/words.txt",Words)
    print("==========================================")

# Tokens  34427
# Words  34427
# Items  8464
# Done
# ==========================================
# Tokens  7126
# Words  7120
# Items  2470
# Done
# ===========================================