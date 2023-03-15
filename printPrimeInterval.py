# Python program to print all prime number in an interval that a user prefers
def disp_Prime(num1, num2): # defining a function disp_Prime 
	#the function takes in two parameters 
    prime_List = []
	for i in range(num1, num2):
		if i == 0 or i == 1:
			continue
		else:
			for j in range(2, int(i/2)+1):
				if i % j == 0:
					break
			else:
				prime_List.append(i)
	return prime_List
# Driver program
starting_Num = int(input('Enter the starting range: '))
ending_Num = int(input('Enter the ending range: '))
lst = disp_Prime(starting_Num, ending_Num)
if len(lst) == 0:
	print("There are no prime numbers in this range")
else:
	print("The prime numbers in the given range are: ", lst)
#This is how the output looks like 
#Enter the starting range: 5
#Enter the ending range: 25
#The prime numbers in this range are: [5, 7, 11, 13, 17, 19, 23]




