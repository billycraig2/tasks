# TASK 1 - Write a python code with accepts the below input and return the given output
message = input("Input: ").lower
message_dict = {}

# looping through each letter of the input 
for letter in message:
    # condition to check if the letter already exists in dict
    if letter in message_dict.keys():
        message_dict[letter] = message_dict[letter] + 1
    else:
        message_dict[letter] = 1

# printing the frequency of each letter in the message
for key in message_dict:
    print("Frequency of " + key + " is " + str(message_dict[key]))



# TASK 2 - Find the largest word from the given input statement
# gets the longest word from a string
def longest_word(message):
    # joins letters that are spaces or alphabet to a string
    words = "".join(filter(lambda c : c.isspace() or c.isalpha(), message))
    split_words = words.split() # split by space into a list

    # loops through words and compares lengths
    longest_word = reduce(lambda a, b: a if len(a) > len(b) else b, split_words)
    return longest_word
    
message = input('Input: ')

print(longest_word(message))



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



# TASK 4 - Find the data from list of dict with name as input 
input = input("Input: ").lower()
dicts = [
    { "name": "Tom", "age": 10 },      
    { "name": "Mark", "age": 5 },      
    { "name": "Pam", "age": 7 },      
    { "name": "Nick", "age": 12 }
]

correct_data = list(filter(lambda person: person["name"].lower() == input, dicts))
print(correct_data[0])



# TASK 5 - Sort the given array of numbers
input = [1,2,3,2,2,2,3,1,1]

# go through each element if the element to the right is bigger it swaps them
def sort_list(input):
    for i in range(len(input)):
        for j in range(len(input)-i-1):
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1], input[j]
            else:
                continue

    print(input)

sort_list(input)


sorted_list = sorted(input)
print(sorted_list)



# TASK 6 - Return the name and savings of the the person with highest savings 
# Function to find the person with the highest savings
def highest_savings(data):
    highest_saving = 0
    highest_savers = []

    # Loop through the data dictionary to get each person's salary and expenditure
    for person, details in data.items():
        salary = details['salary']
        expenditure = details['expenditure']
        savings = salary - (expenditure['rent'] + expenditure['medical'])

        # Check if the current person has the highest savings
        if (savings > highest_saving):
            highest_saving = savings
            highest_savers = [person]
        elif savings == highest_saving:
            highest_savers.append(person)

    return highest_savers, highest_saving

data = {
    "sandy":{
        "salary":50000,
        "expenditure":{"rent":1000,"medical":4000}
        },
    "dheeraj":{
        "salary":500001,
        "expenditure":{"rent":6000,"medical":4000}
        },
    "Pratik":{
        "salary":500001,
        "expenditure":{"rent":6000,"medical":4000}
        }
        }

highest_savers, highest_saving = highest_savings(data)
print(str(highest_savers) + " has the most savings with " + str(highest_saving) + " saved")



# TASK 7 - Rotate the values of the array
def reverse_list(input):
    # go through each element and swap to position
    for i in range(len(input)//2):
        j = len(input) - 1 - i
        input[i], input[j] = input[j], input[i]

    return input


input = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(input))