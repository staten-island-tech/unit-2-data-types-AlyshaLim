""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
    print(values[0])
    print(values[6])
 """
""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" y=input("give me a sentence") #input in terminal to type in and writes give me a sentence 
print(y) #prints the word in terminal
y= y.split(" ") #splits into words
print(len(y)) #prints the length of the sentence by words """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """

""" 
temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" #Challenge 1
x = int(input("give me a number"))
if (x%2) == 0:
    print("even")
else:
    print("odd") """

""" #Challenge 2
x = int(input("Subtotal"))
Service = input("How was the service?")
if Service == ('bad'):
    print(float(x))
elif Service == ('okay'):
    print(float(x*1.15))
elif Service == ('good'):
    print(float(x*1.20))
elif Service == ('great'):
    print(float(x*1.25)) """

""" #Challenge 3 
def allfactors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors 
number = int(input("Please enter a number: "))
listfactors = allfactors(number)
print(listfactors) """

#Challenge 4

import math 

def find_gcf(a, b):
    return math.gcd(a, b)

a = int(input("1"))
b = int(input("Emter"))

gcf = find_gcf(a, b)
