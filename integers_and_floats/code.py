# Arithmetic Operators: 
# Addition +
# Subtraction - 
# Multiply * 
# Division /
# Floor division //
# Modulus %
# Exponent (Power) num**powerValue

num = 30 # setting an integer variable

print(type(num)) # checking type of a variable


num_2 = 10.75 # setting a floating variable
print(type(num_2))

a=19
b=20
print('Sum: ', a+b)
print('Subtract: ', b-a)
print('Multiply: ', 3*5)
print('Divide: ', 21/3)
print('Floor Divide: ', 21//4)
print('Modulus: ', 29%4)
print('Exponent: ', 3**2)


num = 2
num = num + 2
print(num)


num = 2
num+=3
print(num)

num = 3
num *= 3
print(num)


num_3= 3.56
print(round(num_3))
print(round(num_3,1))


# Comparisons: 
# Equal == 
# Less than a < b
# Less or equal a <= b
# Greater than a > b
# Greater or equal a >= b


print ( num_2 > num_3 )  # True
print ( num_2 == num_3 )  # False
print ( num_2 != num_3 )  # True
print ( num_2 < num_3 )  # False
print ( num_2 >= num_3 )  # True
print ( num_2 <= num_3 )  # False


# String into integer

num1 = '200'
num2 = '300'

print(num1 + num2) # 200300 

num1 = int(num1)
num2 = int(num2)

print(num1+num2) # 500