"""
Takes care of cleaning the comments
"""
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
    # filename1="E:\GitHub\Offensive-language-detection\Phase_2_DataPreprocessing\InitialDataset\offensiveDataSet.txt"
    # filename2="E:\GitHub\Offensive-language-detection\Phase_2_DataPreprocessing\InitialDataset\safeDataSet.txt"
    # badData = methods.readFromFile(filename1)
    # safeData = methods.readFromFile(filename2)
    # # safeData = methods.prepareForNLTK(safeData)
    # # badData = methods.prepareForNLTK(badData)
    # safeData = methods.cleanComments(safeData)
    # badData = methods.cleanComments(badData)
    # methods.writeToFile("CleanComments/cleanSafeComments.txt", safeData)
    # methods.writeToFile("CleanComments/cleanBadComments.txt", badData)

    # Clean comments phase2
    filename1="../Phase_1 _DataColector/ColectingPhase2/allComments.txt"

    data = methods.readFromFile(filename1)
    # safeData = methods.prepareForNLTK(safeData)
    # badData = methods.prepareForNLTK(badData)
    cleanData = methods.cleanComments(data)
    methods.writeToFile("../Phase_1 _DataColector/CommentsColected/readyForAdnotation.txt", cleanData)
    wordCounter("../Phase_1 _DataColector/CommentsColected/readyForAdnotation.txt")

#TODO
#lematizare pt limba romana (dexonline)
#ro-word-net
