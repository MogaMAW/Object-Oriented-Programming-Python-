#Python program to check whether the given year is leap year or not

def LeapYear(Year):  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("The given Year is a leap year");  
  else:  
    print ("The given Year is not a leap year")  
Year = int(input("Enter the year to check whether a leap year or not: "))  
LeapYear(Year) 



