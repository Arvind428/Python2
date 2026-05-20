"""
lists is an ordered sequence of elements that can be comprised of strings
Lists are mutable
use zero based index
"""
#index based accessing
cities=["Los Angeles","London","Tokyo"]
i=cities[0]
print(i)#Los Angeles

#negative index accessing
n=cities[-1]
print(n)#Tokyo

#list constructor
name="Arvind"
lc=list(name)
print(lc)

#Len() function= tells the lenght of list 
ln=len(name)
print(ln)

#To update values in an list
#we can use the index number for updating purpose
languages=['python','rust','HTML','node']
languages[0]='Java'
print(languages)

#if we try to update the value with an index number
#which is out of the index present then we get an 
#IndexError

# languages[10]='css'


#  File "c:\Users\arvin\OneDrive\Desktop\python2\day1\list.py", line 34, in <module>
#     languages[10]='css'
#     ~~~~~~~~~^^^^
# IndexError: list assignment index out of range


#del keyword
#del keyword can be used to delete the element inside the list

del languages[0]
print(languages)

#in keyword
#used to check if an element is inside the list

x='HTML' in languages
print(x)

#nested lists
#we can access the elements using the index based accesing
#to access the list inside the list we can use double index based access
# like this companies[2][1] 
companies=['amazon','google',['python','java','aws','asure']]
c=companies[2]
ci=companies[2][0]
print(c)
print(ci)

#unpacking the values inside an list
li=["name",20,"Backend Developer"]
name,age,job=li
print(name)#name
print(age)#20
print(job)#Backend developer

#asterisk(*) operator
name,*rest=li
print(rest)
print(name)#name


#value Error
#we get an value error 
#if number of variables on the left side
#doesnot match the total numbers of items in the list

# name,age,job,city=li

#     name,age,job,city=li
#     ^^^^^^^^^^^^^^^^^
# ValueError: not enough values to unpack (expected 4, got 3)


#SLice Operator(:)
# the slice operatror is used to access protions of list
rollno=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
t=rollno[1:4]#uses index numbers
print(t)
#only even numbers
e=rollno[1::2]#acess every second number in a list
print(e)

"""
this are the comments
3 quotes
"""