#natural number > 1
'''which has only 2 fctors 1 and itself 19=1 and 19 so it is prime number
where 28 having=1,2,4,7,14,28 it is not a prime number because it having more than two factors
    to check wheather the given number is prime or not the first thing it is greater than 1 or not if it is a greater than one than we have to check thr given number having two factors
    .if it is not more than two factors then it is not a prime number'''
    
num=5
count=0
if num>1:
    for i in range(1,num+1):
        if(num%i)==0:
            count=count+1
    if count==2:
        print("number is prime")
    else:
        print("the number is not a prime number")    