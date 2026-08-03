#Array common patterns
  # 1.Traversing 
  # 2.Minimum/Maximum
  # 3.Counting frequency
  # 4.Two pointers


#Reverse an array using two pointers pattern
def reverse_array(arr):
    left= 0 
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
array = [1, 2, 3, 4, 5 , 6]
print("Before:", array)
print("After:", reverse_array(array))

# ** an interview question:  how to reverse an array using two pointers pattern.

#Counting frequency of elements in an array using dictionary
def count_frequency(arr):
    tally_sheet = [0]*10

    #traverse the array 
    for digit in arr:
        tally_sheet[digit] += 1
    #print the tally sheet
    for i in range(10):
        if tally_sheet[i] > 0:
            print(f"Digit {i} appears {tally_sheet[i]} times.")


array = [1, 2, 3, 4, 5, 6, 1, 2, 3]
count_frequency(array)

