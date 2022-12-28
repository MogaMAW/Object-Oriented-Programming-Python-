def hello():
     print("Hey")
     print("It is ")
     print("Thursday")
    
hello()   
hello()
hello()

#the program will print three times because the hello() has been called three times 

# def statements with parameters
# the function is a signed a parameter to be printed  

def hello(name):
    print("Hello " + name)
    
hello("Alice")
hello("Mary")

#parameters are variables that contain arguments 

#define, call, pass, Argument, Parameter\
    
#Define: to define a function is to create it 
#Pass: send  a sting value to a function
#Argument: is the value being passed to a function during a function call
#Parameter: are variables that contain arguments 

#returning Values and return statements
#return value: is the value that a function call evaluates to.
#a return statement consists of a return keyword and the values or expression that the function should return 
#When an expression is used with a return statement, the return value is what this expression evaluates to. 

import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
