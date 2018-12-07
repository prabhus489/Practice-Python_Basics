
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
def Prime_Check(n1,n2):
    if n1 > 1 and n2:
        for i in range(n1,n2):
            if (n1 % i & n2 % i) == 0:
                print("")
                break
            else:
                print("is a prime number")
