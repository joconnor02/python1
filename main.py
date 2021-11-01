def user_input():
    input_string = input("Enter a string")
    return input_string

def backwards(string):
    return string[::-1]

def shredder(string):
    return string[::3]

print(shredder(backwards(user_input())))

