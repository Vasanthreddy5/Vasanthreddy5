#swapping two numbers

'''num1=input("Enter the num1 value:")
num2=input("Enter the num2 value:")

print("value of num1 before swapping:",num1)
print("value of num2 before swapping:",num2)

#here we can do this swappimg by two methods
#1)using temp variable
#2)using assinging variables

#using approach method 1

temp=num1
num1=num2
num2=temp

print("value of num1 after swapping:",num1)
print("value of num2 after swapping:",num2)'''

#by using the second method
num1=20
num2=10

num1,num2=num2,num1
print("value of num1 after swapping:",num1)
print("value of num2 after swapping:",num2)