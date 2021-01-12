#ohamilton79
#06/01/2020
#Circular queue - array-based implementation

#Create a new circular queue of a certain maximum size
def create(maxSize):
    #Array to store data values in queue
    dataArray = [None] * maxSize

    #Points to the front of the queue (initially -1, as there are no items in the queue)
    headPointer = -1

    #Points to the back of the queue (initially -1, as there are no items in the queue)
    tailPointer = -1

    #Return the state of the queue
    return (dataArray, headPointer, tailPointer, maxSize)

#Returns true if queue is empty
def isEmpty(queueState):
    #Unpack queue state
    dataArray = queueState[0]
    headPointer = queueState[1]
    tailPointer = queueState[2]
    maxSize = queueState[3]

    #If both the head and tail pointers equal -1, the queue is empty
    if headPointer == -1 and tailPointer == -1:
        return True

    else:
        return False

#Returns true if the queue is full
def isFull(queueState):
    #Unpack queue state
    dataArray = queueState[0]
    headPointer = queueState[1]
    tailPointer = queueState[2]
    maxSize = queueState[3]

    #If the tail pointer is one less than the head pointer, the queue is full
    if (tailPointer + 1) % maxSize == headPointer:
        return True

    else:
        return False

#Add an item to the end of the queue
def enqueue(newItem, queueState):
    #Unpack queue state
    dataArray = queueState[0]
    headPointer = queueState[1]
    tailPointer = queueState[2]
    maxSize = queueState[3]

    #If the queue is empty, initialise both the head and tail pointers to 0
    if isEmpty(queueState):
        headPointer = 0
        tailPointer = 0
        dataArray[headPointer] = newItem

    #If the queue is full, display an error
    elif isFull(queueState):
        print("Enqueue operation cannot be performed - queue is full")

    #Otherwise, increment the tail pointer (modulo queue size) and add the item there
    else:
        tailPointer = (tailPointer + 1) % maxSize
        dataArray[tailPointer] = newItem

    #Return updated queue state
    return (dataArray, headPointer, tailPointer, maxSize)

#Remove an item from the front of the queue
def dequeue(queueState):
    #Unpack queue state
    dataArray = queueState[0]
    headPointer = queueState[1]
    tailPointer = queueState[2]
    maxSize = queueState[3]

    #If the queue is empty, display an error
    if isEmpty(queueState):
        print("Dequeue operation cannot be performed - queue is empty")

    #If the queue contains a single item, mark the queue as empty by setting pointers to -1
    elif headPointer == tailPointer:
        headPointer = -1
        tailPointer = -1

    #Otherwise, remove an item by incrementing the head pointer (modulo queue size)
    else:
        headPointer = (headPointer + 1) % maxSize

    #Return updated queue state
    return (dataArray, headPointer, tailPointer, maxSize)

#Get the element at the front of the queue and output it
def peek(queueState):
    #Partially unpack queue state
    dataArray = queueState[0]
    headPointer = queueState[1]

    #If the queue isn't empty...
    if not isEmpty(queueState):
        #Get the item pointed to by the head pointer
        frontItem = dataArray[headPointer]

        #Output it
        print(frontItem)

    #...otherwise, output an error
    else:
        print("Peek operation cannot be performed - queue is empty")
    
"""queueState = create(10)
queueState = enqueue("John", queueState)
queueState = enqueue("Josh", queueState)
queueState = enqueue("John", queueState)
queueState = enqueue("Josh", queueState)
queueState = dequeue(queueState)
queueState = dequeue(queueState)
queueState = enqueue("John", queueState)
queueState = enqueue("Josh", queueState)
queueState = enqueue("John", queueState)
queueState = enqueue("Josh", queueState)
queueState = enqueue("Billy", queueState)
queueState = enqueue("Jack", queueState)
queueState = enqueue("James", queueState)
queueState = enqueue("Jill", queueState)
queueState = enqueue("Jared", queueState)
queueState = dequeue(queueState)
queueState = dequeue(queueState)
queueState = dequeue(queueState)
queueState = dequeue(queueState)
queueState = dequeue(queueState)
queueState = dequeue(queueState)
queueState = dequeue(queueState)
queueState = dequeue(queueState)
queueState = dequeue(queueState)
queueState = dequeue(queueState)
peek(queueState)

print(queueState[2])"""
        
