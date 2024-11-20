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