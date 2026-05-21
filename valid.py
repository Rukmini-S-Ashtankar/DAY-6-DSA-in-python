# # WAP to check if a string containing parentheses is valid.
# while True:
#     para = input("Enter something: ")
#     newpara = ""
#     if para ==  ("", "{([])}"):
#        print("Valid!")
#        break
#     else:
#         print("Invalid")

# =========================     +++++     =========================
def isValid(s: str) -> bool:
    stack = []
    # Map closing brackets to their corresponding opening brackets
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            # Pop the top element if stack isn't empty, else use a dummy value
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            # It's an opening bracket, push it onto the stack
            stack.append(char)
            
    # If the stack is empty, all brackets were matched correctly
    return not stack

# Examples
print(isValid("()[]{}")) # Output: True
print(isValid("([)]")) # Output:                                 # wrong program