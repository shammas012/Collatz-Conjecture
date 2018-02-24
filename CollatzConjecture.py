# Author : Mohamed Shammas Mohamed Ali Manaf; 
# Date   : 2018-02-06
# Program : The Collatz Conjecture
# References : https://en.wikipedia.org/wiki/Collatz_conjecture
#             https://docs.python.org/3/tutorial/inputoutput.html
#             https://www.peterbe.com/plog/interesting-casting-in-python


#fetching the start value from the user
n = int(input('Please enter the starting value for the Collatz Conjecture :'))
print(n)

while n > 1: # loop will execute only if the number is greater than 1
 if n%2==0: # checking if the number is even
  n/=2      # dividing the even number by 2
 else:
  n = (3*n) + 1 
 print(int(n))   # display the number (casting applied to avoid decimal places) in the end of each looping

#Output
#For instance, if the start value as 17, then output will be as follows:

# c:\GMIT\Scripting\Collatz>python CollatzConjecture.py
# Please enter the starting value for the Collatz Conjecture :17
#17
#52
#26
#13
#40
#20
#10
#5
#16
#8
#4
#2
#1
