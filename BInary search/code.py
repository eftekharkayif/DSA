def binary_search(my_list, target_number):
    low= 0
    high= len(my_list) - 1

    while low <= high:
        mid= (low + high) // 2
        print(f"Low: {low}, High: {high}, Mid: {mid}, Guess: {my_list[mid]}")  # Debugging line
        guess= my_list[mid]

        if guess == target_number:
            return mid
        if guess > target_number:
            high= mid - 1
        else:
            low= mid + 1

    return -1
numbers= [1, 3, 5, 7, 9]
print(binary_search(numbers, 3))  # Output: 1