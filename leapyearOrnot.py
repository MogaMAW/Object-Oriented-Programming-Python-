#Python program to check whether the given year is leap year or not
# Function implementation to check leap year  
def LeapYear(Year): 
    #Condition to check if the given year is leap year or not  

  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("The given Year is a leap year"); 
    
    # Else it is not a leap year  
  else:  
    print ("The given Year is not a leap year")
    # Taking an input year from user  

Year = int(input("Enter the year to check whether a leap year or not: "))  
# Printing the leap year result  

LeapYear(Year) 



