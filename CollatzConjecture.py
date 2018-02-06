#Author : Mohamed Shammas Mohamed Ali Manaf; Date : 2018-02-06
#Program : The Collatz Conjecture

#fetching the start value from the user
n = int(input('Please enter the starting value for the Collatz Conjecture :'))
print(n)

while n > 1: # loop will execute only if the number is greater than 1
 if n%2==0: # checking if the number is even
  n/=2      # dividing the even number by 2
 else:
  n = (3*n) + 1 
 print(int(n))   # display the number (casting applied to avoid decimal places) in the end of each looping
