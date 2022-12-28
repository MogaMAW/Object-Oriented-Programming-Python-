//a python program to get  a user's name and weight then displays the age basing on a fixed birth_year
def person(name,birth_year,weight):
    age = 2002-birth_year
    if name == "": #if no name has been entered
        print("\n name : name" , "\n weight : ",weight, "\n birthdate : ",birth_year)
        print("\n age" , age)
    else:
        print("\n name : ", name ,"\n weight : ", weight, "\n birthdate : ",birth_year,"\n age" , age)
        
def main():
    name = input("Enter the name :") #let the user enter their name.
    weight = float(input("Enter the weight: "))
    birth_year = 2002     //is a fixed year       
    #making all the users have same birth_date of 2002
    
    person(name,birth_year, weight)
    
main()
        
              
