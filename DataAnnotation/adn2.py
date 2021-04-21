"""
Script for removing comment smaller than 100 characters
"""
import fileinput


def writeToFile(filename,inputData):
    prefix = "../DataAnnotation/CommentsForAnnotations2/"
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
        data = data.split('<ANNOTATION = >\n')
    f.close()
    for comm in data:
        if len(comm) < 100:
            data.remove(comm)
            print(comm)
    print(data)
    writeToFile(filename,data)


if __name__ == '__main__':
    prefix='../DataAnnotation/CommentsForAnnotations/CDataset'
    ext='.txt'
    # for index in range(1,16):
    #     filename=prefix+str(index)+ext
    #     removeComments(filename)
    removeComments("../DataAnnotation/CommentsForAnnotations/CDataset1.txt")
    removeComments("../DataAnnotation/CommentsForAnnotations/CDataset2.txt")
    removeComments("../DataAnnotation/CommentsForAnnotations/CDataset3.txt")
    removeComments("../DataAnnotation/CommentsForAnnotations/CDataset4.txt")
    removeComments("../DataAnnotation/CommentsForAnnotations/CDataset5.txt")
    removeComments("../DataAnnotation/CommentsForAnnotations/CDataset6.txt")
    removeComments("../DataAnnotation/CommentsForAnnotations/CDataset7.txt")
    removeComments("../DataAnnotation/CommentsForAnnotations/CDataset8.txt")
    removeComments("../DataAnnotation/CommentsForAnnotations/CDataset9.txt")
    removeComments("../DataAnnotation/CommentsForAnnotations/CDataset10.txt")
    removeComments("../DataAnnotation/CommentsForAnnotations/CDataset11.txt")
    removeComments("../DataAnnotation/CommentsForAnnotations/CDataset12.txt")
    removeComments("../DataAnnotation/CommentsForAnnotations/CDataset13.txt")
    removeComments("../DataAnnotation/CommentsForAnnotations/CDataset14.txt")
    removeComments("../DataAnnotation/CommentsForAnnotations/CDataset15.txt")


