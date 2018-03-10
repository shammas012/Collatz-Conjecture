# Author: Mohamed Shammas Mohamed Ali Manaf 
# Date : 2018-03-10
# Description : Python script containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial
# References : https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html
#			   https://www.calculatorsoup.com/calculators/discretemathematics/factorials.php
#			   https://www.python-course.eu/recursive_functions.php	
			  

# Defininition of factorial function
def factorial(number):

	number += 1;
	while number > 0:
		
		# assign the previous integer in numerical order to the "number" variable
		number -= 1					
		# calling the factorial function recursively.			
		 		
		if number == 0:
			return 0
			break;
		elif number == 1:
			return 1
			break
		else:
    			return (number * factorial(number-1))		
		
print("factorial of 5, 5! is ",factorial(5))
print("factorial of 7, 7! is ",factorial(7))
print("factorial of 10, 10! is ",factorial(10))
		
		
