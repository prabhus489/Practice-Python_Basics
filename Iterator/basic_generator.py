#Noramal Function
def function_a():
    return "a"


#generator function
def generator_a():
    yield "a"


print(function_a())
print(generator_a())

#Output will be shown like below
#a ----> function_a()
#<generator object generator_a at 0x000001D8B9EA4A20>  -----> generator_a()

