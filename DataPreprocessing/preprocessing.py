import methods
def wordCounter(filename):
    file = open(filename, 'r')
    count = 0
    for line in file:
        line = line.strip("\n")
        words = line.split()
        count += len(words)
    file.close()
    print(count)

if __name__ == '__main__':

    # # Clean comments
    # filename1="E:\GitHub\Offensive-language-detection\DataPreprocessing\InitialDataset\offensiveDataSet.txt"
    # filename2="E:\GitHub\Offensive-language-detection\DataPreprocessing\InitialDataset\safeDataSet.txt"
    # badData = methods.readFromFile(filename1)
    # safeData = methods.readFromFile(filename2)
    # # safeData = methods.prepareForNLTK(safeData)
    # # badData = methods.prepareForNLTK(badData)
    # safeData = methods.cleanComments(safeData)
    # badData = methods.cleanComments(badData)
    # methods.writeToFile("CleanComments/cleanSafeComments.txt", safeData)
    # methods.writeToFile("CleanComments/cleanBadComments.txt", badData)

    # Clean comments phase2
    filename1="../DataColector/ColectingPhase2/allComments.txt"

    data = methods.readFromFile(filename1)
    # safeData = methods.prepareForNLTK(safeData)
    # badData = methods.prepareForNLTK(badData)
    cleanData = methods.cleanComments(data)
    methods.writeToFile("../DataColector/ColectingPhase2/readyForAdnotation.txt", cleanData)
    wordCounter("../DataColector/ColectingPhase2/readyForAdnotation.txt")

#lematizare pt limba romana (dexonline)
#ro-word-net
