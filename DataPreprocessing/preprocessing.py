import methods

if __name__ == '__main__':

    # Clean comments
    filename1="E:\GitHub\Offensive-language-detection\DataPreprocessing\InitialDataset\offensiveDataSet.txt"
    filename2="E:\GitHub\Offensive-language-detection\DataPreprocessing\InitialDataset\safeDataSet.txt"
    badData = methods.readFromFile(filename1)
    safeData = methods.readFromFile(filename2)
    # safeData = methods.prepareForNLTK(safeData)
    # badData = methods.prepareForNLTK(badData)
    safeData = methods.cleanComments(safeData)
    badData = methods.cleanComments(badData)
    methods.writeToFile("CleanComments/cleanSafeComments.txt", safeData)
    methods.writeToFile("CleanComments/cleanBadComments.txt", badData)



#lematizare pt limba romana (dexonline)
#ro-word-net
#eliminare cuvinte mai mari de 16 caractere