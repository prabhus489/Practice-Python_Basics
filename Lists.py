friends_list = ['Akhil', 'James','Amir']
travel_list = ['perfume', 'clothes','money']

print(friends_list)

#list as constants

movies = ["Ice Age", "Twlight", "Harry Potter"]
print(movies)

#list function
# creating empty list using list fuction
movies_1 = list()

#adding values to list
movies_1.append("Die Another Day")
movies_1.append("Tiger")
movies_1.append("Narnia")
print(movies_1)

#differnt types of elements in a list
mov = ["ravanan",0, "manimegalai", 1, "kaviya", 2]
print(mov)

#accessing list using indexes

print(mov[0])
print(mov[1])
print(mov[2])

#list index out of bound range

#print(mov[6])

#accessing list using negative indexes

print(mov[-1])
print(mov[-2])
print(mov[-3])

#Slicing a part of list
print(mov[0:2])

print(mov[0:6])
print(mov[0:5])

print(mov[:])

mov[1] = '007'

print (mov)

msm = ["lux", "lifeboy", "hamam"]
msm[0:2] = []
print(msm)

#Cloning of list

a = [1,2,3]
b = a[:]
print (a, b)
print (a is b)
#a & b are refering to the same element but are not refering to the same object

x = [4,5,6]

y = x

#a & b are refering to the same element and also same object

print (x is y)

#List membership
q = [11,12,13]

print(11 in q)

print(11 not in q)

#list operations(+,*)

#concatenate
w = [14,15,16]
r = q+w
print (r)

#repeat
print (r*2)

#list & for loop
friends = ["Ram", "lax", "Prabhu"]
for friend in friends:
    print(friend)

#Enumerate a list

for (i,v) in enumerate(friends):
    print(i,v)

#Nested List

nested = ["ramya", "kumar", [1,2,3,4]]
print(nested[2])

n = nested[2]

print (n[1])

print(nested[2][0])

#matrices as a nested list

mx = [[1,2,3],[4,5,6],[7,8,9]]
print(mx[0])

print[mx[1][2]]

#List Comprehension
#create a list of squares

sq=[]
for x in range(5):
    sq.append(x**2)
print (sq)

squares = list(map(lambda x: x**2, range(5)))

print (squares)

numbers = [1,2,3,4,5,6,7,8]
doubled_odds = []
for n in numbers:
    if n%2==1:
        doubled_odds.append(n**2)
print (doubled_odds)

