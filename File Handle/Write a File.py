f1 = open("new.txt", "a")
f1.write("Python , C, Javascript\n")
f1.close()

#open and read the file after the appending:
f2 = open("new.txt", "r")
print(f2.read())