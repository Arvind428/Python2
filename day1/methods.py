"""
Common Methods used for Lists 
"""

#append()
#used to add elements at the end of the list
#also can add list inside a list

num=[1,2,3,4,5]
print(num)
num.append(6)
print(num)

#list inside a list

evn=[2,4,6]
num.append(evn)
print(num)

#extend
#used to add multiple elements from one lsit to another
num.extend(evn)
print(num)

#insert()
#used to insert elements at a particular index
#syntax 
#var.insert(index,value)

num.insert(2,500)
print(num)