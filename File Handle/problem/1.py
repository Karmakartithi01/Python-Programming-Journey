"""
1. Write a function in python to read the content from a text file "poem.txt" line by line and display the same on screen

"""
# def read_file(filename):
#     try:
#         with open(filename, "r") as f:
#             content = f.read()
#             print(content)
#             print()
#             f.close()
#         print("Content----- " +     content + " ------ has been read successfully")
#     except IOError:
#                 print("Content has not been read successfully")

# if __name__ == "__main__":
#     src = input("Enter the Book name : ")
#     book = src+".txt"
#     read_file(book)


"""
Solution 2 ::

def read_file():
    file = open("poem.txt","r")
    for line in file:
        print(line, end="")
    file.close()

read_file()
"""