# Function to check prime number  

def PrimeChecking(num): 
        # Condition to check given number is more than 1  
    if num > 1:  
        for i in range(2, int(num/2) + 1):  
            if (num % i) == 0:  
                print("The number ",num, "is not a prime number")  
                break  
        else:  
            print("The number ",num, "is a prime number")  
    else:  
        print("The number ",num, "is not a prime number")  
num = int(input("Enter a number to check prime or not: "))  
PrimeChecking(num)  



