"""
Script for removing comment smaller than 100 characters
"""
import fileinput


def writeToFile(filename,inputData):
    prefix = "E:/GitHub/Offensive-language-detection/RawCommentsForAnnotations/"
    filename = filename.split('/')
    file=filename[len(filename)-1]
    with open(prefix+file,"w+", encoding="utf-8") as f:
        for comm in inputData:
            if comm!='\n' and len(comm.strip()) > 100:
                f.write('<ANNOTATION = >\n')
                f.write(str(comm))
    f.close()
    print("Done")

def removeComments(filename):
    with open(filename, "r+", encoding="utf-8") as f:
        data = f.read()
        data = data.split('<ANNOTATION=>\n')
    f.close()
    for comm in data:
        if len(comm) < 100:
            data.remove(comm)
            print(comm)
    print(data)
    writeToFile(filename,data)


if __name__ == '__main__':
    # prefix='E:/GitHub/Offensive-language-detection/RawCommentsForAnnotations/RawDataset'
    # ext='.txt'
    # for index in range(1,16):
    #     filename=prefix+str(index)+ext
    #     # open(filename, "x")
    # removeComments("E:/GitHub/Offensive-language-detection/DataColector/ColectingPhase2/allComments.txt")
    removeComments("/DataColector/RawCommentsForAnnotations/RawDataset1.txt")
    removeComments("/DataColector/RawCommentsForAnnotations/RawDataset2.txt")
    removeComments("/DataColector/RawCommentsForAnnotations/RawDataset3.txt")
    removeComments("/DataColector/RawCommentsForAnnotations/RawDataset4.txt")
    removeComments("/DataColector/RawCommentsForAnnotations/RawDataset5.txt")
    removeComments("/DataColector/RawCommentsForAnnotations/RawDataset6.txt")
    removeComments("/DataColector/RawCommentsForAnnotations/RawDataset7.txt")
    removeComments("/DataColector/RawCommentsForAnnotations/RawDataset8.txt")
    removeComments("/DataColector/RawCommentsForAnnotations/RawDataset9.txt")
    removeComments("/DataColector/RawCommentsForAnnotations/RawDataset10.txt")
    removeComments("/DataColector/RawCommentsForAnnotations/RawDataset11.txt")
    removeComments("/DataColector/RawCommentsForAnnotations/RawDataset12.txt")
    removeComments("/DataColector/RawCommentsForAnnotations/RawDataset13.txt")
    removeComments("/DataColector/RawCommentsForAnnotations/RawDataset14.txt")
    removeComments("/DataColector/RawCommentsForAnnotations/RawDataset15.txt")


