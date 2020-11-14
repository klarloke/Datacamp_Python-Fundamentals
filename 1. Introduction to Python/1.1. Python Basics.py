## PYTHON AS A CALCULATOR

# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# How much is your $100 worth after 7 years (if you can earn 10% annual interest)?
print(100 * (1.1 ** 7))


## VARIABLE ASSIGNMENT & CALCULATIONS WITH VARIABLES

# Create a variable savings
savings = 100

# Create a variable growth_multiplier
growth_multiplier = 1.1

# Calculate result
result = savings * (growth_multiplier ** 7)

# Print out result
print(result)


## OTHER VARIABLE TYPES

# Create a variable desc (string)
desc = 'compound interest'

# Create a variable profitable (boolean)
profitable = True


## OPERATIONS WITH OTHER TYPES

savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Assign product of growth_multiplier and savings to year1
year1 = savings * growth_multiplier

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc as a concatated string
print(doubledesc)



## TYPE CONVERSION

# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)
