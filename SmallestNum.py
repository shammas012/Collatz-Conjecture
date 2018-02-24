# Author: Mohamed Shammas Mohamed Ali Manaf 
# Date : 2018-02-24
# Description : Program that calculates the smallest number divisible evenly by all numbers between 0 and 20
# References : https://www.programiz.com/python-programming/break-continue
#	       https://www.pythoncentral.io/pythons-range-function-explained/
# Note : The program took almost 3 minutes to display the o/p because of the volume of loops involved.

smallestNum = 0 										# variable to assign the smallest number
intValue = 0											# variable for iterating over the integers; starting at zero
while smallestNum == 0: 								# this while loop will iterate through all integers until the smallest evenly divisble number is found
	#print(i)
	for divisor in range(1,21):							# the range returns the list of integers from 1 to 20
		if intValue % divisor == 0: 					# check if number contained in the current "intValue" is evenly divisble by the "divisor"
			if divisor == 20 and intValue % divisor == 0: # assume if the divisor is 20, at this stage the "intValue" should be divisible by all integers preceeding the "divisor" in numerical order.
				smallestNum = intValue					  # assign the current value in intValue to smallestNum
				break;
		else:
			break;										# break the looping if the value in intValue is not evenly divisble by any of the elements in the range list.
	intValue+=1											# increment the value of intValue by 1
print('The smallest number evenly divisible by all number bewteen and incluing 1 and 20 is : ',smallestNum)										# Display value
		
# Output of the program is follows:
# c:\GMIT\Scripting\Week5 -- Smallest Number divisible>python SmallestNum.py                                                              
# The smallest number evenly divisible by all number bewteen and incluing 1 and 20 is :  232792560  
