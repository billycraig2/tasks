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
