	
# Conside a list,
# n = [1, 2, 4, 2, 5, 8]
# Find the index of first duplicate in this list.


# def first_duplicate_index(arr):

#     seen = set()
#     for index, value in enumerate(arr):
#         if value in seen:
#             return index,value
#         seen.add(value)
#     return -1  # Return -1 if no duplicate is found
# Array = [1, 2, 4, 2, 2, 5, 6,]
# result = first_duplicate_index(Array)
# print('First duplicate (index, value):', result)


def first_duplicate_index(arr):
    # This function takes a list (arr) and finds the position (index)
    # of the FIRST number that appears more than once.
    # If no number repeats, it will return -1.

    duplicate_indices = set()
    # Create an empty "set" — think of it like a bag that stores
    # values we've already seen. A set never allows duplicate items
    # inside it, and checking "is this already in here?" is very fast.

    for index, value in enumerate(arr):
        # Loop through the list one item at a time.
        # enumerate() gives us TWO things at once for each item:
        #   - index -> the position of the item in the list (0, 1, 2, ...)
        #   - value -> the actual number at that position

        if value in duplicate_indices:
            # Check: have we already put this exact value in our bag before?
            # If yes, that means this is a REPEATED number.

            return index
            # We found a repeat! Immediately stop the function and
            # give back the index (position) where the repeat happened.

        duplicate_indices.add(value)
        # If the value was NOT a repeat, add it to our bag now,
        # so that if we see it again later, we'll recognize it.

    return -1
    # If the loop finishes and we never found a repeated number,
    # return -1 to mean "no duplicates found in this list."


# ---- Example usage ----

Array = [1, 2, 4, 4, 2, 5, 6, 4, 5, 5, 6, 7, 3, 2, 5, 6, 7, 6, 8, 8, 4, 3, 2, 2, 1]
# A sample list of numbers to test the function on.

first_duplicate_index(Array)
# This line calls the function, but doesn't do anything with the result
# because it's not stored in a variable or printed.
# (It's basically wasted work — see note below!)

print('first_duplicate_index:', first_duplicate_index(Array))
# This line calls the function AGAIN (a second time) and this time
# prints the result to the screen, labeled clearly.
