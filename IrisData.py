# Author: Mohamed Shammas Mohamed Ali Manaf 
# Date : 2018-03-04
# Description : Print the petal length, petal width, sepal length and sepal width from the Iris Data DataSet to the terminal, 
#				with the decimal places aligned, with a space between the columns
#References : https://stackoverflow.com/questions/1025379/decimal-alignment-formatting-in-python
#
			  

# Opens the file IrishData.csv
with open('Data\IrisData.csv') as input:
	#iterate through each line in the file
	for line in input:
		#format and display to the terminal, "1.1f" applied because the dataset seems to have only one number before and after the decimal point
		#print('{0:.1f}  {0:.1f}  {0:.1f}  {0:.1f}'.format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))
		print('{}  {}  {}  {}'.format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))
