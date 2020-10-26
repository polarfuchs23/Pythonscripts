import xlsxwriter

wb = xlsxwriter.Workbook('C:/Users/Joshua/Documents/Tabellen/YourTablesName.xlsx')

# Create a table with the name in the brackets
tab = wb.add_worksheet("The tables name")

# Define variables
# E.g. x = 0
Summe = 0
# Create first row
tab.write(0, 0, "Index")
tab.write(1, 0, '1')

# Write a cell by following scheme for every variable
# If you use a for statement add one to the first parameter
# tab.write(0, "Index of variable", "Name of variable")

# Write a cell by following scheme for every variable
# If you use a for statement add one to the first parameter
# tab.write(1, "Index of variable", "Value of Variable")

"""
# Standard for
tab.write(0, 1, 'i')
for i "Your statement":
	# Your statement here
	# Standard code
	tab.write(i+1, 0, str(i+1))
	tab.write(i+1, 1, str(i+1))
	# Write a cell by following scheme for every variable
	# tab.write(i+1, "Index of variable+1", "Value of variable")
"""

"""
# Standard while
counter = 1
while "Your statement":
	counter += 1
	tab.write(counter, 0, str(counter))
	# Your statement here

	# Write a cell by following scheme for every variable
	# tab.write(counter, "Index of variable", "Value of variable")
"""
# Write the rest

# After changing a variable write after following scheme
# tab.write("The new rows number - 1", 0, "The current row you are in - 1")
# and for every variable
# Add one to the variables index if you used for
# tab.write("The new rows number - 1", "Index of variable", "Value of variable")

wb.close()