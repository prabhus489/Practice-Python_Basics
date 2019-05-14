num = int(input("enter a number: "))

for i in range(2, int(num / 2)):
    if num % i == 0:
        print("not prime number")
        break
else:
    print("prime number")