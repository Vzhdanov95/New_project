"""
Arithmetic Operators
Relational Operators
Logical Operators
Membership and Identity Operator
Bitwise Operators
Warlus Operator

"""

# Arithmetic Operators
add_oper = 4 + 5 # Addition
subtr_oper = 5 - 4 # Subtraction
mult_oper = 40 * 4 # Multiplication
div_oper = 32 / 1.5 # Division
mod_oper = 32 % 1.5 # Modulus (divides and left the remainder) Остаток
expon_oper = 20 ** 2 # Exponent (power calc. on operators) Степень
trunc_floor_div_oper = 40 // 12 # Truncation or Floor Division returns the division of operands
                                # where result is quotient Целочислительн дел 

# Relational or Comparison Operators 
age = 16
required_age = 18
eq_to_oper = age == required_age # Equal to (==)
not_eq_oper = age != required_age # Not equal to (!=)
great_th_oper = age > required_age # Greater than (>)
less_th_oper = age < required_age # Less than (<)
great_or_equa_per = age >= required_age # Greater than or equal to (>=)
less_or_equa_oper = age <= required_age # Less than or equal to (<=)


# Logical operators
x = True
y = False
print('x and y is', x and y) # both values are True
print('x or y is', x or y) # at least one value is True
print('x and y is', not x) # not True, check if False


# Membership and Identity Operator
course = "philology"
print('x' in course) # returna True if the value is found in the sequence
print('p' in course)
print('u' not in course) # returna True if the value is not found in the sequence

num = 5
print(id(num)) # id() check the memory adress where value is stored
num1 = 7
num2 = 7
num3 = 4
print(id(num1))
print(id(num2))
print(id(num3))
print(num1 is num2) # returns True if the operands are identical 
print(num1 is num3) # returns True if the operands are not identical

larger_num = 455
larger_num1 = 455
print(larger_num is larger_num1)
print(larger_num1 is not larger_num1)

# Warlus(Морж) operator - new assignment expression

surname1 = "Ivanchuk"
print(surname1)

print(surname:="Ivanchuk") # warlus combines declaration and implement.



