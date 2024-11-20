import re

# TASK 3 - Take an array of strings as input and segregate them to ipv4 and ipv6 using regex.
# uses regex to print if email is valid
def check_email(email):
    # checks string with regex
    if re.search(r'\b[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{2,7}\b', email):
        print("Valid email")
    else:
        print("Invalid email")


email = input("Enter email: ")
check_email(email)

# number="255"
# print(re.search(r""))