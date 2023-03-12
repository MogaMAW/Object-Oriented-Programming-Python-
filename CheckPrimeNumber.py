# Function to check prime number  

def PrimeChecking(num): 
        # Condition to check given number is more than 1  
    if num > 1:  
          # For look to iterate over the given number  
        for i in range(2, int(num/2) + 1):  
             # Condition to check if the given number is divisible  
            if (num % i) == 0:  
                   #If divisible by any number it's not a prime number
                print("The number ",num, "is not a prime number")  
                break  
        # Else print it as a prime number  
        else:  
            print("The number ",num, "is a prime number")  
   # If the given number is 1  
    else:  
        print("The number ",num, "is not a prime number") 
# Input function to take the number from user  

num = int(input("Enter a number to check prime or not: "))  

# To print the result, whether a given number is prime or not  

PrimeChecking(num)
#Output1 of the above Python program to check the prime number
#Enter a number to check prime or not: 10





