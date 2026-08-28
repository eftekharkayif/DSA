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
