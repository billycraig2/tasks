import re


# uses regex to print if email is valid
def check_email(email):
    # checks string with regex
    if re.search(r'\b[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{2,7}\b', email):
        return 'Valid email'
    else:
        return 'Invalid email'


#email = input("Enter email: ")
#check_email(email)

# number="255"
# print(re.search(r""))
