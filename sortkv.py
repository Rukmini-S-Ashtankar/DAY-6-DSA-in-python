# Q:- Write a function to sorT a dictionary by keys or values in ascending or descending order.
# Logic:- Use the sorted() function with a custom key or use list comprehension.
# Sample input:- {"C":3, "B":2, "A":1}
# Expected Output:- (Ascending by key) { "A":1, "B":2, "C":3}
# Expected Output:- (Descending by key) { "C":3, "B":2, "A":1}

def sort_dict(d, by="key", reverse=False):
    index = 0 if by == "key" else 1
    return dict(sorted(d.items(), key=lambda x: x[index], reverse=reverse))


# Sample input
data = {"C": 3, "B": 2, "A": 1}

# Ascending by key
print(sort_dict(data))
# Output: {'A': 1, 'B': 2, 'C': 3}

# Descending by key
print(sort_dict(data, reverse=True))
# Output: {'C': 3, 'B': 2, 'A': 1}

# Ascending by value
print(sort_dict(data, by="value"))
# Output: {'A': 1, 'B': 2, 'C': 3}                           # cgt