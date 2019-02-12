with open("files/new.txt", "w") as file:
    file.write("\n Hello world!!!")
    file.write("\n World hello!!")
    file.write("\n Hello!!!")
    file.write("\n World!!!")
    pass

with open("files/new.txt", "r") as file:
    fullFile = file.read()
    print(fullFile)
    