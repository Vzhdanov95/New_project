# create a password restrictions for users
# 1) Password should consist of minimum 8 characters
# 2) Password should have at least one capital letter
# 3) Password should have at least 1 integer in it

password_field = input("Enter your password: ")
passwrord_digits = any(char.isdigit() for char in password_field) # any() returns checks whenever each element of sequence is True

if len(password_field) < 8:
    print("Sorry. Your password has less then 8 characters")
elif password_field.islower():
    print("Sorry. Your password should have at least one capital letter")
elif not passwrord_digits:
    print("Sorry. Your password should at least have one integer")
else:
    print("Congrats. You have entered a valid password.")

####################################################### it's just a instance of my code