"""
functions are the reusable pieces of codes 
we can call them when we need to write the same code 
functions help us to avoid repetive coding and can be implemented again and again 
example: the print is a function in the python 

We also have built in functions in the python like input()
"""

# name=input("what is your name: ")
# print('The name is ',name)

def hello():
    print("Hello Arvind")
hello()

def sum(a,b):
    print(a+b)
sum(12,1)
#sum() if we call the functions without giving the correct amount of parameters
# then we get an TypeError 
"""
We can use the return keyword to exit the function and return a value.
if we dont use return keyword in python the default value is None
"""

#SCOPE

"""
Local scope (L): Variables defined in functions or classes.

Enclosing scope (E): Variables defined in enclosing or nested functions.

Global scope (G): Variables defined at the top level of the module or file.

Built-in scope (B): Reserved names in Python for predefined functions, modules, keywords, and objects.
"""
#Local scope means that a variable declared inside a function or class can only be accessed within that function or class.
def my_func():
    my_var = 10#locally scoped to my_func
    print(my_var)
my_func()
#print(my_var) gives name erroe cuz the my_var is defined but cant be accessed by the outer variable

#Enclosing scope means that a function that's nested inside another function can access the variables of the function it's nested within

"""
def outer_func():
    msg = 'Hello there!'
    print(res)

    def inner_func():
        res = 'How are you?'
        print(msg)

    inner_func()

outer_func() # NameError: name 'res' is not defined
"""
"""
res cannot be acceses by the outer function because the res in locally scoped 
and the outer fucntion is trying to print the res even before the interpreter reads the res variable
"""

"""
We can avoid this issue by intializing the res as empty string
then use 'nonlocal' key word for res which makes the res as the nonlocal variable
"""
def outer_func():
    msg = 'Hello there!'
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(res)  # Now res is accessible and modified

outer_func()
# Output:
# Hello there!
# How are you?

#Global scope refers to variables that are declared outside any functions or classes which can be accessed from anywhere
# in the program. Here, my_var can be accessed anywhere, even inside a function it's not defined in:

my_var = 100

def show_var():
    print(my_var)

show_var() # 100
print(my_var) # 100

"""
And if you want to make a locally scoped variable defined inside a function globally accessible
you can use the global keyword:
"""
my_var_1 = 7

def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_vars() # 7 10

# my_var_2 is now a global variable and can be accessed anywhere in the program
print(my_var_2) # 10


#You can also use the global keyword to modify a global variable:

my_var = 10  # A global variable

def change_var():
    global my_var  # Allows modification of a global variable
    my_var = 20

change_var()

print(my_var)  # my_var is now modified globally to 20


#Finally, built-in scope refers to all of Python's
#built-in functions, modules, and keywords, and are available anywhere in your program: