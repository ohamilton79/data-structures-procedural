#ohamilton79
#29/12/2020
#Queue - array-based implementation

#Create a new queue of a certain maximum size
def create(maxSize):
    #Array to store data values in queue
    dataArray = [None] * maxSize

    #Points to the front of the queue (initially -1, as there are no items in the queue)
    headPointer = -1

    #Points to the back of the queue (initially -2, as there are no items in the queue)
    tailPointer = -2

#Add an item to the queue (enqueue it)
def enqueue(newItem, dataArray, headPointer, tailPointer, MAXSIZE):
    #1. Check if the enqueue operation can be performed
    if tailPointer < MAXSIZE - 1:
        #2. If the queue is empty, set both the head and tail pointers to 0
        if headPointer > tailPointer:
            headPointer = 0
            tailPointer = 0

        #3. Otherwise, increment the tail pointer
        else:
            tailPointer +=1

        #4. Insert the new item at the position given by the updated tail pointer
        dataArray[tailPointer] = newItem

    #5. If the enqueue operation can't be performed (queue is full), output an error
    else:
        print("Enqueue operation can't be performed - queue is full")

    #Return updated queue state
    return (dataArray, headPointer, tailPointer, MAXSIZE)


#Remove an item from the queue (dequeue it)
def dequeue(dataArray, headPointer, tailPointer, MAXSIZE):

    #1. Check if the dequeue operation can be performed (queue isn't empty)
    if tailPointer >= headPointer:
        #2. Increment the head pointer, so the item at the front of the queue is removed
        headPointer += 1

    #3. If the dequeue operation can't be performed (queue is empty), output an error
    else:
        print("Dequeue operation can't be performed - queue is empty")

    #Return updated queue state
    return (dataArray, headPointer, tailPointer, MAXSIZE)

#Read the item at the front of the queue
def peek(dataArray, headPointer, tailPointer, MAXSIZE):
    #1. Check that the queue isn't empty
    if tailPointer >= headPointer:
        #2. Get the value at the index given by the head pointer and return it
        headValue = dataArray[headPointer]
        return headValue

    #3. Otherwise, output an error
    else:
        print("Peek operation can't be performed - queue is empty")
        return None

dataArray, headPointer, tailPointer, MAXSIZE = enqueue("Craig", dataArray, headPointer, tailPointer, MAXSIZE)
enqueue("Dave", dataArray, headPointer, tailPointer, MAXSIZE)
enqueue("Sam", dataArray, headPointer, tailPointer, MAXSIZE)
print(peek(dataArray, headPointer, tailPointer, MAXSIZE))
dequeue(dataArray, headPointer, tailPointer, MAXSIZE)
print(peek(dataArray, headPointer, tailPointer, MAXSIZE))
dequeue(dataArray, headPointer, tailPointer, MAXSIZE)
print(peek(dataArray, headPointer, tailPointer, MAXSIZE))
dequeue(dataArray, headPointer, tailPointer, MAXSIZE)
print(peek(dataArray, headPointer, tailPointer, MAXSIZE))
enqueue("John", dataArray, headPointer, tailPointer, MAXSIZE)
print(peek(dataArray, headPointer, tailPointer, MAXSIZE))
print(dataArray, dataArray, headPointer, tailPointer, MAXSIZE)
print(headPointer, dataArray, headPointer, tailPointer, MAXSIZE)
print(tailPointer, dataArray, headPointer, tailPointer, MAXSIZE)
