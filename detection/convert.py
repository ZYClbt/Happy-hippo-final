def updatefile(file, old_str, new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


updatefile("train.txt", "lhj/train/", "")
updatefile("val.txt", "lhj/valid/", "")
