my_stack = []
#Push Elements
my_stack.append("BOOK-1")
my_stack.append("BOOK-2")
my_stack.append("BOOK-3")
print(my_stack)

# Peek/top of the stack
print("Top of the stack:", my_stack[-1])

#Pop elements
print( "pop the top of the stack:", my_stack.pop())

#is Empty, Check if stack is empty 
if len(my_stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")
# reverse a string using stack
def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str

# Example usage
print(reverse_string("Hello, World!"))