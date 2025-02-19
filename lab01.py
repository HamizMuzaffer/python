## Question 1 
n = float(input("Enter your temperature: "))

def celtoF(n):
    temp = 9/5*n +32 
    print(temp)
celtoF(n)

##  Question 2 

password  = str(input("Enter your password: "))
def reverseF(password):
    passwordReversed = password[::-1]
    print(passwordReversed)

reverseF(password)
    

## Question 3 

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def checkEven(numbers):
    for i in numbers:
        if(i%2 == 0):
            print(i)

checkEven(numbers)

