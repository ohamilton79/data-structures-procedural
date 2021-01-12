#ohamilton79
#27/12/2020
#Linked list - array-based implementation

#Create a new linked list of a certain maximum size
def create(maxSize):
    #Array to store data values in linked list
    dataArray = [None]*maxSize
    #Array to store pointers to next indices in list
    pointersArray = [None]*maxSize
    #Points to the first item in the linked list
    headPointer = None
    #Points to free space in linked list
    freePointer = 0

    return (dataArray, pointersArray, headPointer, freePointer)

#Add a new item to the beginning of the linked list
def addItem(newItem, dataArray, pointersArray, headPointer, freePointer): 
    #1. Store data at address given by the free storage pointer
    dataArray[freePointer] = newItem

    #2. Update free pointer
    oldFreePointer = freePointer
    if pointersArray[freePointer] != None:
        freePointer = pointersArray[freePointer]

    else:
        freePointer += 1

    #3. If the list isn't empty, get the new item to point to the item previously at the beginning of the list
    if headPointer != None:
        pointersArray[oldFreePointer] = headPointer

    #4. Set the head pointer to the new item
    headPointer = oldFreePointer

    return (dataArray, pointersArray, headPointer, freePointer)

#Remove an item from the beginning of the linked list
def removeItem(dataArray, pointersArray, headPointer, freePointer):
    #1. Mark the position of this item as free space
    oldFreePointer = freePointer
    freePointer = headPointer
    #2. Get the position pointed to by the item to be removed
    nextPointer = pointersArray[headPointer]
    #3. Set the head pointer to this position
    oldHeadPointer = headPointer
    headPointer = nextPointer

    #4. Make the removed item point to the free space
    pointersArray[oldHeadPointer] = oldFreePointer

    return (dataArray, pointersArray, headPointer, freePointer)

#Traverse the linked list
def traverse(dataArray, pointersArray, headPointer, freePointer):
    #1. Start at the head pointer (start of list)
    currentNodePointer = headPointer

    #2. Keep traversing until the current node is free space
    while currentNodePointer != None:
        #3. Get the value at this position and output it
        nodeValue = dataArray[currentNodePointer]
        print(nodeValue)

        #4. Set the node pointer to the position pointed to by this node
        currentNodePointer = pointersArray[currentNodePointer]

    return (dataArray, pointersArray, headPointer, freePointer)

#Search for and output the item if found
def search(item, dataArray, pointersArray, headPointer, freePointer):
    #1. Start at the head pointer (start of list)
    currentNodePointer = headPointer

    counter = 0

    #2. Keep traversing until the current node is free space or the item is found
    while currentNodePointer != None:
        #3. Get the value at this position
        nodeValue = dataArray[currentNodePointer]

        #4. If the value at this position equals the data item being searched for, output it and exit
        if nodeValue == item:
            print("'{}' found".format(item))
            #Return the index of the item
            return counter

        #5. Set the node pointer to the position pointed to by this node
        currentNodePointer = pointersArray[currentNodePointer]

        counter += 1

    #6. Output 'Not found' if the item doesn't exist in the list
    print("'{}' not found".format(item))

#Remove an item at a specific index
def removeAt(index, dataArray, pointersArray, headPointer, freePointer):
    #1. If index is 0, the item is being removed from the front of the list
    if index == 0:
        return removeItem(dataArray, pointersArray, headPointer, freePointer)
    
    else:
        #2. Iterate over index - 1 items from the start
        count = index - 1
        pointer = headPointer
        
        while count != 0:
            #Get the pointer pointed to by this node
            pointer = pointersArray[pointer]

            count-= 1

        #3. Bypass the node to be deleted by assigning the pointer of the previous node to the next node
        previousPointer = pointer
        currentPointer = pointersArray[pointer]
        nextPointer = pointersArray[currentPointer]

        #If there is a next node to point to
        if nextPointer != None:
            pointersArray[previousPointer] = nextPointer

        #Otherwise, set a null pointer
        else:
            pointersArray[previousPointer] = None

        #5. The deleted node is now free space
        oldFreePointer = freePointer
        freePointer = currentPointer
        #6. Get the new free pointer to point to the old one
        pointersArray[freePointer] = oldFreePointer

    return (dataArray, pointersArray, headPointer, freePointer)

#Insert an item at a specific index
def insertAt(index, newItem, dataArray, pointersArray, headPointer, freePointer):   
    #1. If index is 0, the item is being inserted at the front of the list
    if index == 0:
        return addItem(newItem, dataArray, pointersArray, headPointer, freePointer)

    else:
        #2. Iterate over index - 1 items from the start
        count = index - 1
        pointer = headPointer

        while count != 0:
            #Get the pointer pointed to by this node
            pointer = pointersArray[pointer]
            count -= 1

        #3. Insert the new item in the location pointed to by the free space pointer
        dataArray[freePointer] = newItem

        #4. Get the previous node to point to this new node, and the new node to point to the next node
        previousPointer = pointer
        nextPointer = pointersArray[pointer]

        #If there is a next node to point to
        if nextPointer != None:
            pointersArray[freePointer] = nextPointer

        #Otherwise, set a null pointer
        else:
            pointersArray[freePointer] = None

        #Get the previous node to point to the new node
        pointersArray[previousPointer] = freePointer
        
        #5. Update free pointer
        if pointersArray[freePointer] != None:
            freePointer = pointersArray[freePointer]

        else:
            freePointer += 1

    return (dataArray, pointersArray, headPointer, freePointer)

"""#TEST DATA

addItem("Dave")
#traverse()
addItem("Craig")
#traverse()
removeAt(1)
#traverse()
#search("Craig")
#search("Dave")
addItem("Sam")
print(dataArray)
#traverse()
#insertAt(1, "James")
print(dataArray)
print(pointersArray)
print(freePointer)
print(headPointer)
traverse()"""

