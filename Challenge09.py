#!/usr/bin/python3
#Cristiano Garcia
#19/10/2023

print("1 and 2")

print("\nIs it equal?")
number = 1 == 2 
print(number)

print("\nIs it not equal?")
number = 1!= 2
print(number)   

print("\nIs it less than?")
number = 1 < 2
print(number)

print("\nIs it less than or equal?")
number = 1 <= 2
print(number)

print("\nIs it greater than?")
number = 1 > 2
print(number)   

print("\nIs it greater than or equal?")
number = 1 >= 2 
print(number)

#Elif statement 
if number == True:
    print("The number is greater than or equal to 2")
elif number == False:
    print("The number is less than 2")
else:
    print("Invalid input")

#And
if number > 1 and number < 3:
    print("\nThe number is between 0 and 3")
else:
    print("\nThe number is not between 0 and 3")

#Or statement 
if number < 0 or number > 10:
    print("\nThe number is outside the range of 0 to 3")
else:
    print("\nThe number is between 0 and 10")

    
