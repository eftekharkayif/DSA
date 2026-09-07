from collections import deque
n = int(input("Enter N: "))
queue = deque()       
queue.append("1")
for i in range(n):
    current = queue.popleft()
    # print(current, end = " ")
    queue.append(current + "0")
    queue.append(current + "1") 


print("Original queue: ", queue)
stack = []
while queue: 
    stack.append(queue.pop())
print("Reversed queue: ", stack)













