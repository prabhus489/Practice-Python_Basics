num1 = int(input("Enter an integer for num1 :   "))
num2 = int(input("Enter an integer for num2 to print prime number upto this number :  "))
lists = []
print("The prime numbers between ", num1, " and ", num2, " are: ", end=" ")

def prime_number():
    for num in range(num1 + 1, num2 + 1):

        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                lists.append(num)
    print(lists)
    print(lists[1])
prime_number()
