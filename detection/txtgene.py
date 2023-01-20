import os

file_path = "D:/study/22fa/cv/final-project/Happy-hippo/yolov5-7.0/datasets/mydataset/train/labels"
path_list1 = os.listdir(file_path)


def saveList(pathName):
    for file_name in pathName:
        with open("dataset_path/train.txt", "a") as f:
            f.write("D:/study/22fa/cv/final-project/Happy-hippo/yolov5-7.0/datasets/mydataset/images/" + file_name[:-4] + ".jpg" + "\n")


saveList(path_list1)
