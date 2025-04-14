# type()
age = 45
name = "Alexander"
is_logged_in = False

print(type(age))
print(type(name))
print(type(is_logged_in))

username = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = int(input("Please enter your height: "))

if height == age:
    print(False)
else:
    print(True)

print(type(username))
print(type(age))
print(type(age == username))