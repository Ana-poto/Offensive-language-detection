import fileinput
import os

from ipython_genutils.py3compat import xrange


def remove_empty_lines(f1,f2):
    f=open(f2,'w+')
    for line in fileinput.FileInput(f1, inplace=1):
        if line.rstrip():
            f.write(line)
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
    # remove_empty_lines("../DataColector/ColectingPhase2/readyForAdnotation.txt","../DataAnnotation/CommentsForAnnotations/comments.txt")
    # file = open("../DataAnnotation/CommentsForAnnotations/comments.txt", 'r')
    # #214383
    # path = '../DataAnnotation/CommentsForAnnotations'
    # # Specify the file name
    # file = "CDataset"
    # extension = ".txt"
    #
    # # Creating 15 files at specified location
    # for i in range(1,16):
    #     filename=file+str(i)+extension
    #     with open(os.path.join(path, filename), 'w') as fp:
    #       pass
    wordCounter("VocabularAnnotation/comments.txt")