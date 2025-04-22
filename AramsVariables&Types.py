#  AramsVariables&Types.py will show ability to add, subtract, multiply, and divide using defined variables
#     Created by Aram Asman
#        Creation Date: 04/22/2025
#        Last Edit: 04/22/2025

var_I = 10000
var_II = 3
var_III = 0
#using var = # should pair each word with a defined value for performing math.
# var is being used as a shortening for variable here

# this part is addition
adding = var_I + var_II
print(adding)
#this should print an output value of 10003 if the code adds correctly.

# now subtraction
subtracting = var_I - var_II
print(subtracting)
# the output here should print 9997

# onto multiplication
multiply_1 = var_II * var_I
print(multiply_1)
# output value should be 30000
multiply_2 = var_I * var_III
print(multiply_2)
# this output should equal 0

# finally, division
dividing = var_I / var_II
print(dividing)
# this should print 3333 due to / rounding to an integer for 
# the output without a float
# dividing by zero unsurprisingly gives an error message, as dividing 
# by zero is not possible in math

# printing "hello world!" using addition
var1 = ("hello")
var2 = ("world")
helloworld = var1 + " " + var2 + "!"
print(helloworld)
# when substituting subtraction for the division, it causes an error

# working with a float
var_I_float = float(var_I)
print(var_I)
print(var_I_float)
# this changes var_I from 10000 to 10000.0, adding a decimal value
# attempting to float a string value causes an error, as it is not 
# set to a numerical value
