# is_gratuated = True

# x = 9
# y = 10

# is_equal = x==y

# not_equal = x != y

# print(not_equal)

# print(x <= y)
# print(x >= y)

# print(x < 10 and x > -5)

# print (not is_gratuated)

# print(bool("Hello"))
# print(bool(1))

##############################################
# x = 10
# if x > 0:
#     print("x is positive")
# elif x < 0:
#     print("x is negative")
# else:
#     print("x is zero")

# b = 10
# z = 20

# if b > 0 and z > 0:
#     print("both are True")

# some_message = "Your message"

# if some_message: #bool(some_message)
#     print("message is not empty")

# year = 2025

# if year % 4 == 0 and year % 100 != 0:
#     print("year is leap(высокосный)")
# elif year % 400 == 0:
#     print("year is leap(высокосный)")
# else:
#     print("year is not leap(высокосный)")

######################################################

animal = "Tiger"
kind = "- Predator"

print(len(animal))
print(len(kind))
print(len(""))


the_beast_is = animal + " " + kind
print(type(the_beast_is))

some_number = 10
some_string = str(some_number)
print(type(some_string))

random_string = int("10")
print(type(random_string))

# check_here = int(input("Enter a number:"))
# print(type(check_here))

big_integer = 2 ** 1000
print(len(str(big_integer))) # количество цифр в 2 ** 1000 через len() и str()

test_if_tiger_there = "Tiger is a big hunter"
print("Tiger" in test_if_tiger_there)

make_up_str = "Doctor"
print(make_up_str.upper())
print(make_up_str.capitalize())
print(make_up_str.lower())
print(make_up_str.count("o"))

string_with_spaces = "  Big spaces  "
print(len(string_with_spaces))
print(len(string_with_spaces.strip()))
print(string_with_spaces.strip())  

age = 30
name = "Voland"

print(f"{name} is {30}")

my_string = input("Enter your number: ")

if my_string.isdigit():
    my_integer = int(my_string)
    print(my_integer)
else:
    print(f"{my_string} is not a number")
    