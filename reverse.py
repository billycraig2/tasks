# TASK 7 - Rotate the values of the array

# reverses the elements of an array
def reverse_list(input):
    # go through each element and swap to position
    for i in range(len(input)//2):
        j = len(input) - 1 - i
        input[i], input[j] = input[j], input[i]

    return input


input = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(input))