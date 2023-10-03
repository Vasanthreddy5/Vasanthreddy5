#check the given number is prime number or not

#logic for code
#natural number >1,which has only 2 factors 1 and itself
#19=1 and 19->it is prime number
#28=1,2,4,7,14,28->it is not a prime number
'''to check weather the number is prime or not :first thing it is greater than 1 or not if it is greater than 1 then we have to check the number
having two factors.if it is more than two factors then it is not a prime number'''

#--------------------code------------------------#

num=5
count=0
if num>1:
    for i in range(1,num+1):
        if(num%i)==0:
            count=count+1
    if count==2:
        print("the given number is prime")
    else:
        print("the given number is not prime")