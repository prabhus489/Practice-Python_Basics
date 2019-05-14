#method1
def Secondlargest():
    list = [10,30,20,45,55,96,36,43,23,98,78,58,76]
    list.sort()
    result = list[-2]
    return result

print(Secondlargest())

#method2
list1 = [10, 20, 4, 45, 99]
def SecLarge(list1):
    new_list = set(list1)
    new_list.remove(max(new_list))
    res = max(new_list)
    return res

print(SecLarge(list1))


