	
# Conside a list,
# n = [1, 2, 4, 2, 5, 8]
# Find the index of first duplicate in this list.


def first_duplicate_index(arr):

    seen = set()
    for index, value in enumerate(arr):
        if value in seen:
            return index,value
        seen.add(value)
    return -1  # Return -1 if no duplicate is found
Array = [1, 2, 4, 2, 2, 5, 6,]
result = first_duplicate_index(Array)
print('First duplicate (index, value):', result)