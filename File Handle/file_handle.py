import os
def create_file(filename):
    try:
        with open(filename, "x") as f:
            print("File "+ filename + " ------- has created succesfully.")
    except IOError:
        print("File "+ filename + " ------- has not created succesfully.")

def read_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(content)
        print("Content ---- "+ content + " ------ has been read successfuly")
    except IOError:
        print("Content ---- "+ content + " ------ has not been read successfuly")

def write_file(filename):
    try:
        with open(filename, "a") as f:
            txt = "Hello World"
            f.write(txt)
        print("Text :---- "+ txt + " ------- has added succesfully.")
    except IOError:
        print("Text :----  has not added succesfully.")

def overwrite_file(filename):
    try:
        with open(filename, "w") as f:
            txt = "Hi Good Evening"
            f.write(txt)
        print("Text :---- "+ txt + "------- has changed succesfully.")
    except IOError:
        print("Text :----  has not changed succesfully.")

def rename_file(filename, newfilename):
    try:
        os.rename(filename, newfilename)
        print("FileName :  "+ filename + " has changed to -- "+ newfilename + "------- succesfully.")
    except IOError:
        print("FileName :  "+ filename + " ------- has  not changed to succesfully.")

def delete_file(filename):
    try:    
        os.remove(filename)
        print("FileName :  "+ filename + " ------- has been deleted succesfully.")
    except IOError:
        print("FileName :  "+ filename + " ------- has not available")


if __name__ == '__main__': 
    
    filename = "newfile.txt"
    newfilename = "newnew.txt"
    overwrite_file(filename)
    read_file(filename)
    rename_file(filename, newfilename)
    delete_file(newfilename)
