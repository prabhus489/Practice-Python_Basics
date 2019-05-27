# Normal Function
def function_a():
    return "a"


# Generator function
def generator_a():
    yield "a"


print(function_a())   # It will print the value called by using return keyword
print(generator_a())  # It will not print anything in console. It will show only the object location

# Output will be shown like below
# a ----> function_a()
# <generator object generator_a at 0x000001D8B9EA4A20>  -----> generator_a()

'''
next() : Asking the generator what the next item is ( It will return the object value stored using "yield" Keyword
yield : Yield are used in Python generators. 
        A generator function is defined like a normal function, but whenever it needs to generate a value, 
        it does so with the yield keyword rather than return. If the body of a def contains yield, 
        the function automatically becomes a generator function. 
'''

print(next(generator_a()))  # It will directly call the generator function and asks for the next item stored using yield
# output:
# "a"

print(next(generator_a()))  # It will directly call the generator function and asks for the next item stored using yield
# output:
# "a"
print(next(generator_a()))  # It will directly call the generator function and asks for the next item stored using yield
# output:
# "a"

'''
In the above print function we are using next(generator_a()) 
(ie, we're calling generator function directly by using next() keyword. 
So every time when we call the print function with next(generator_function())(ie, print(next(generator_a()))
It will go and ask for the first item stored in first yield object  
and always looks for the first yield keyword and return the output of the first object in yield. 
because we're calling the generator function itself directly. 
So for each and every time it is exectuing the function from the start. 
so it will end with executing first yield keyword
In order to make use of the yield keyword and generator function we need to store the generator function in one variable
and call the variable using next keyword(ie,var = generator_function() and  print(next(var))).
To understand the best use of generator function please goahead and see the below code & explaination.
'''

# Now defining generator function with more than 1 yield


def sp_generate():
    yield "a"
    yield "b"
    yield "c"

# Now we'll call the generator function directly inside next() keyword and see what will happen


print(next(sp_generate()))  # It will call first yield only (ie, yield "a")

'''
Output:
"a"
'''


print(next(sp_generate()))  # It will call first yield only (ie, yield "a")

'''
Output:
"a"
'''

print(next(sp_generate()))  # It will call first yield only (ie, yield "a")

'''
Output:
"a"
'''

# Now lets store the generator function in variable and see what happens!

# Storing Generator function in a variable

xyz = sp_generate()

print(next(xyz))  # If we call xyz (ie, variable) with next() keyword.
# It will execute and print first object stored using yield (ie, yield "a")

'''
output:
"a"
'''

print(next(xyz))  # for the second time. It will execute and print object stored using  second yield (ie, yield "b")

'''
output:
"b"
'''

print(next(xyz))  # for the third time. It will execute and print object stored using  third yield (ie, yield "c")

'''
output:
"c"
'''

print(next(xyz))  # for the fourth time. when it try to execute and print object stored using fourth yield
# It will throw exception  as StopIteration(Traceback Error).
# Because we don't have  fourth yield in our code.

'''
output:
StopIteration
'''


