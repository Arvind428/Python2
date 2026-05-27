#Over the next few lessons we are going to learn about lists, tuples, and ranges, which are three basic sequence types used in Python.
#The list data type is an ordered sequence of elements that can be comprised of strings, numbers, or even other lists. Lists are mutable and use zero-based indexing, meaning that the first element of the list is at index zero.

#syntax =>> file = open("filename", "mode")
#Example =>>file = open("data.txt", "r")

#=================================writing=======================
# if file exists file overwrites 
# if file doesn't -w creates it
# file = open("m1.txt", "w")
# file.write("mentoring 3")
# file.close()

# with open("hi.txt", "w") as file:
#    file.write("hi everyone")

#============================Reading==========================

# file = open("hi.txt", "r")
# print(file.read())
# file.close()


#=========================adding new txt==============================
#we can add new data with existing, if there is no file it will create
# with open("b1.txt", "a") as f:
#     f.write(" python developer\n")


#==========================creation=============
#creates the file if only there is no file with the name mentioned

# file = open("a1.txt", "x")
# file.write("This file is created using x mode.")
# file.close()


#key difference====

# w: creating a file if there no named file otherwise it will overwrites
# a: creating a file if not exists otherwise it will add the new text
# x: creaing a file and if the file exists returns an error


