# Q:- Write a function to find all the elements that appear more than once a list.
# Logic:- Use a loop and a dictionary to count occurences.
# Sample input: [4, 3, 2, 7, 8, 2, 1, 5, 5]
# Expected output: [2, 5]

def find_duplicates(lst):
    count = {}
    duplicates = []

    for item in lst:
        count[item] = count.get(item, 0) + 1

    for item in count:
        if count[item] > 1:
            duplicates.append(item)

    return duplicates


# Sample input
nums = [4, 3, 2, 7, 8, 2, 1, 5, 5]

# Output
print(find_duplicates(nums))                     #cgt
