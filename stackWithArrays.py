#ohamilton79
#29/12/2020
#Stack - array-based implementation

#CONSTANTS
MAXSIZE = 10

#Array to store data values in stack
dataArray = [None] * MAXSIZE

#Points to the top of the stack (initially -1, as there are no items in the stack)
topPointer = -1

#Push an item onto the stack
def push(newItem):
    #Define globals to manipulate stack
    global dataArray
    global topPointer
    global MAXSIZE

    #1. Check that the maximum stack size hasn't been exceeded
    if topPointer < MAXSIZE - 1:
        #2. If it hasn't, increment the top pointer and add the new data item to the array in this position
        topPointer += 1
        dataArray[topPointer] = newItem

    else:
        #4. Otherwise, output an error
        print("Push operation can't be performed - stack is full")


#Pop an item from the stack
def pop():
    #Define globals to manipulate stack
    global dataArray
    global topPointer
    global MAXSIZE

    #1. Check if pop operation can be performed
    if topPointer >= 0:

        #2. If so, decrement the top pointer
        topPointer -= 1

    else:
        #3. Otherwise, output an error
        print("Pop operation can't be performed - stack is empty")



#Return the item at the top of the stack
def readTop():
    #Define globals to access stack
    global dataArray
    global topPointer

    #1. Check if the stack is non-empty
    if topPointer > -1:
        #2. If so, return the item at the index given by the top pointer
        return dataArray[topPointer]

    else:
        #3. Otherwise, output an error
        print("Top operation cannot be performed - stack is empty")
        return None


push("Craig")
push("Dave")
pop()
print(readTop())
print(dataArray)
print(topPointer)
