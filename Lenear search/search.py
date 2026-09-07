#1.linear Search 
subjects = ['Math', 'English', 'Science', 'History', 'Art']
target= "Science"
found = False

for subject in subjects:
    if subject == target:
        print(f"{target} found in the list.")
        found= True
        break

#2. Index of the searched number 


for  i in range(len(subjects)):
    if subjects[i] == target:
        print(f"{target} found at index {i}.")
        found = True
        break

if found == False:
    print("Subject not found.")


    

#Time complexity example:
numbers = [1, 2, 3, 4, 5]
search = int(input("Enter a number to search: "))
found = False
for i in range(len(numbers)):
    if numbers[i] == search:
        print(f"{search} found at index {i}.")
        found = True
        break

if found == False:
    print("Number not found in the list.")






























