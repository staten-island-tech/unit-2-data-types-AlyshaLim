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

""" y = input("give me a sentence") #input in terminal to type in and writes give me a sentence 
print(y) #prints the word in terminal
x = y.split( ) #splits into words
print(len(x)) #prints the length of the sentence by words """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """
"""  """
""" x = "test"
print(f"hello {x}") """


""" temp = 75
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
def allfactors(n):      #defines fuction that takes parameter n 
    factors = []        #defines an empty list to store the factors of n 
    for i in range(1,n+1):  #allows all factors from 1 to n inclusive
        if n%i == 0:        #checks if n is divisible by i, the number used in the loop which indiciates i is a factor of n 
            factors.append(i)   #if i is a factor of n its added to the list of factors 
    return factors  #returns list of factors after end of loop
number = int(input("Please enter a number: "))  #input 
listfactors = allfactors(number)    #calls the allfactors function w the users input and stores the result in list factors 
print(listfactors)  #prints the list of factors by that number """

""" #Challenge 4 
def gcf(x,y):
    great = [] 
    for i in range(1,min(x,y)+1): #python only sees 1 to y not including y so the 1 ensures that they is seen inclusively 
        if x%i == 0 and y%i == 0:
            great.append(i)
    return max(great)
num1 = int(input("Please enter 1st number: "))
num2 = int(input("Please enter 2nd number: "))
greatest = gcf(num1, num2)
print(greatest) """
