#Enqueue : 

#Algorithm to add an element to the end of the queue
# 1. START
# 2. Check if the queue is full.
# 3. If the queue is full, produce overflow error and exit.
# 4. If the queue is not full, increment rear pointer to point 
#    the next empty space.
# 5. Add data element to the queue location, where the rear 
#    is pointing.
# 6. return success.
# 7. END

# Code:
MAX = 6;
intArray = [0] * MAX
front = 0;
rear = -1;
itemCount = 0;
def isFull():
    return itemCount == MAX
def isEmpty():
    return itemCount == 0
def removeData():
    data = intArray[front+1]
    if(front == MAX):
        front = 0
    itemCount-1
    return data
def insert(data):
    global rear, itemCount
    if(not isFull()):
        if(rear == MAX-1):
            rear = -1
        rear = rear + 1
        intArray[rear] = data
        itemCount+1
insert(3);
insert(5);
insert(9);
insert(1);
insert(12);
insert(15);
print("Queue: ")
for i in range(MAX):
    print(intArray[i], end = " ")
while(not isEmpty()):
    n = removeData()
    print(n, end = " ")





#Dequeue :
#Algorithm for dequeue operation in a queue data structure
# 1. START
# 2. Check if the queue is empty.
# 3. If the queue is empty, produce underflow error and exit.
# 4. If the queue is not empty, access the data where front 
#    is pointing.
# 5. Increment front pointer to point to the next available 
#    data element.
# 6. Return success.
# 7. END
 
#Code:
MAX = 6
intArray = [0] * MAX
front = 0
rear = -1
itemCount = 0
def isFull():
    return itemCount == MAX
def isEmpty():
    return itemCount == 0
def insert(data):
    global rear, itemCount
    if not isFull():
        if rear == MAX-1:
            rear = -1
        rear += 1
        intArray[rear] = data
        itemCount += 1
def removeData():
    global front, itemCount
    data = intArray[front]
    if front == MAX-1:
        front = 0
    else:
        front += 1
    itemCount -= 1
    return data
insert(3);
insert(5);
insert(9);
insert(1);
insert(12);
insert(15);
print("Queue: ")
for i in range(MAX):
    print(intArray[i], end = " ")
num = removeData()
print("\nElement removed: ", num)
print("Updated Queue: ")
while(not isEmpty()):
    n = removeData()
    print(n, end = " ")








#Peek:
#The peek() is an operation which is used to retrieve the frontmost element in the queue, without deleting it. This operation is used to check the status of the queue with the help of the pointer.
#Algorithm for peek operation in a queue data structure
# 1. START
# 2. Return the element at the front of the queue
# 3. END

# code:
MAX = 6
intArray = [0] * MAX
front = 0
rear = -1
itemCount = 0
def peek():
    return intArray[front]
def isFull():
    return itemCount == MAX
def insert(data):
    global rear, itemCount
    if(not isFull()):
        if(rear == MAX-1):
            rear = -1
        rear  = rear + 1
        intArray[rear] = data
        itemCount+1
insert(3);
insert(5);
insert(9);
insert(1);
insert(12);
insert(15);
print("Queue: ")
for i in range(MAX):
    print(intArray[i], end = " ")
print("\nElement at front: ", peek())

