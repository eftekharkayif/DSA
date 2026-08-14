def decimal_to_binary(num):
    stack = []
    while num > 0:
        reminder = num % 2
        stack.append(reminder)
        num = num // 2

    binary_string = ""
    while len(stack) > 0:
        binary_string += str(stack.pop())
    return binary_string
print(decimal_to_binary(10))  # Output: 1010 