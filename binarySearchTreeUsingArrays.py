#ohamilton79
#Binary search tree implementation
#31/12/2020

#CONSTANTS
MAXSIZE = 10

#An array storing each data item
data = [None] * MAXSIZE

#An array storing the left pointers for each item
leftPointers = [None] * MAXSIZE

#An array storing the right pointers for each item
rightPointers = [None] * MAXSIZE

#Pointer to the root node of the binary tree
rootPointer = None

#Points to available free space in the binary search tree
# (initially the first space in the array is free)
freePointer = 0


#Returns a Boolean value indicating whether there is space for a value to be inserted into a node
def spaceAvailable(nodeIndex, newItem):
    global data
    if data[nodeIndex] != None:
        #If there is space to the left of this node, and the new item to be added is less than the value of this node...
        if leftPointers[nodeIndex] == None and newItem < data[nodeIndex]:
            return True
        
        #...or if there is space to the right of this node, and the new item to be added is greater than the value of this node
        elif rightPointers[nodeIndex] == None and newItem > data[nodeIndex]:
            return True

    #Otherwise, there is no space available for the new node to be inserted as a child of the current node
    return False

#Add an item to the binary search tree
def addItem(newItem):
    #Define globals so search tree can be manipulated
    global data
    global leftPointers
    global rightPointers
    global rootPointer
    global freePointer
    
    #1 Add the item in the location pointed to by the free pointer
    data[freePointer] = newItem

    #2. If the tree is empty, the item can be added as the root of the tree
    if rootPointer == None:
        rootPointer = freePointer

    #If the tree already contains at least one item
    else:
        #3. Set the root node as the current node
        currentNode = rootPointer

        while not spaceAvailable(currentNode, newItem):
            #4. Traverse to the left if the data item being added is less than the value of this node
            if newItem < data[currentNode]:
                #5. Set this next node as the current node
                currentNode = leftPointers[currentNode]

            #Traverse to the right if the data item being added is greater than the value of this node
            else:
                #5. (same as above)
                currentNode = rightPointers[currentNode]

            #6. Repeat until there is space available for the new item

        #7. Once a suitable node has been found, add the new item to the left if it is less than the value of the node...
        if newItem < data[currentNode]:
            leftPointers[currentNode] = freePointer

        #...or to the right if it is greater than the value of the node
        else:
            rightPointers[currentNode] = freePointer

    #8. Update the free pointer - if more free space is available, the right pointer will point to it
    if rightPointers[freePointer] != None:
        freePointer = rightPointers[freePointer]

    else:
        freePointer += 1

#Remove an item from the binary search tree
def removeItem(itemToRemove):
    #Define globals so search tree can be manipulated
    global data
    global leftPointers
    global rightPointers
    global rootPointer
    global freePointer

    #If the item being removed is the root node
    if itemToRemove == data[rootPointer]:
        pass

    #1. Set current node as root node
    currentNode = rootPointer

    #2. While the current node exists, and isn't the one to delete
    while currentNode != None and data[currentNode] != itemToRemove:
        #a) Set previous node to be current node
        previousNode = currentNode

        #b) If the item to be deleted is less than the current node, traverse the left branch
        if itemToRemove < data[currentNode]:
            currentNode = leftPointers[currentNode]

        #c) Else, if the item to be deleted is greater than the current node, traverse the right branch
        else:
            currentNode = rightPointers[currentNode]

    #3. If the node to be deleted has no children...
    if leftPointers[currentNode] == None and rightPointers[currentNode] == None:
        #a) If current node < previous node, set previous node's left pointer to null
        if data[currentNode] < data[previousNode]:
            leftPointers[previousNode] = None

        #b) Else, if current node >= previous node, set previous node's right pointer to null
        else:
            rightPointers[previousNode] = None

        #Update free space
        oldFreePointer = freePointer
        freePointer = currentNode
        rightPointers[currentNode] = oldFreePointer

    #4. If the node to be deleted has a single child (at least one empty pointer)
    elif leftPointers[currentNode] == None or rightPointers[currentNode] == None:
        #Get the pointer to the child node
        childPointer = None
        if leftPointers[currentNode] != None:
            childPointer = leftPointers[currentNode]

        else:
            childPointer = rightPointers[currentNode]

        
        #a) If the current node is on the left of the previous node
        if leftPointers[previousNode] == currentNode:
            #a) Set the previous node's left pointer to the child node
            leftPointers[previousNode] = childPointer

        #b) If the current node is on the right of the previous node
        if rightPointers[previousNode] == currentNode:
            #a) Set the previous node's right pointer to the child node
            rightPointers[previousNode] = childPointer

        #Update free space
        oldFreePointer = freePointer
        freePointer = currentNode
        rightPointers[currentNode] = oldFreePointer

    #5. If the node to be deleted has 2 children, use Hibbard deletion method
    else:
        rightNode = rightPointers[currentNode]
        #a) If right node has a right subtree...
        if rightPointers[rightNode] != None or leftPointers[rightNode] != None:
            #a) Find smallest leaf node in right subtree
            smallestLeaf = rightNode
            while leftPointers[smallestLeaf] != None:
                smallestLeaf = leftPointers[smallestLeaf]

            #b) Remove the smallest leaf node and update free space
            removeItem(data[smallestLeaf])

            #c) Replace current node with smallest leaf node
            data[currentNode] = data[smallestLeaf]
            #oldFreePointer = freePointer
            #freePointer = smallestLeaf
            #rightPointers[freePointer] = oldFreePointer

#Recursive subroutine to perform a pre-order traversal of the binary search tree
def preOrderTraversal(rootPointer):
    #Define globals so search tree can be accessed
    global data
    global leftPointers
    global rightPointers
    
    #1. Output the data item of the root node of the current subtree
    print(data[rootPointer])

    #2. If the node pointed to by the left pointer of the current root node isn't null, perform a pre-order traversal of the subtree in which this child node is the root node
    if leftPointers[rootPointer] != None:
        preOrderTraversal(leftPointers[rootPointer])

    #3. If the node pointed to by the right pointer of the current root node isn't null, perform a pre-order traversal of the subtree in which this child node is the root node
    if rightPointers[rootPointer] != None:
        preOrderTraversal(rightPointers[rootPointer])


#Recursive subroutine to perform an in-order traversal of the binary search tree
def inOrderTraversal(rootPointer):
    #Define globals so search tree can be accessed
    global data
    global leftPointers
    global rightPointers

    #1. If the node pointed to by the left pointer of the current root node isn't null, perform an in-order traversal of the subtree in which this child node is the root node
    if leftPointers[rootPointer] != None:
        inOrderTraversal(leftPointers[rootPointer])

    #2. Output the data item of the root node of the current subtree
    print(data[rootPointer])

    #3. If the node pointed to by the right pointer of the current root node isn't null, perform an in-order traversal of the subtree in which this child node is the root node
    if rightPointers[rootPointer] != None:
        inOrderTraversal(rightPointers[rootPointer])
    

#Recursive subroutine to perform a post-order traversal of the binary search tree
def postOrderTraversal(rootPointer):
    #Define globals so search tree can be accessed
    global data
    global leftPointers
    global rightPointers

    #1. If the node pointed to by the left pointer of the current root node isn't null, perform a post-order traversal of the subtree in which this child node is the root node
    if leftPointers[rootPointer] != None:
        postOrderTraversal(leftPointers[rootPointer])

    #2. If the node pointed to by the right pointer of the current root node isn't null, perform a post-order traversal of the subtree in which this child node is the root node
    if rightPointers[rootPointer] != None:
        postOrderTraversal(rightPointers[rootPointer])

    #3. Output the data item of the root node of the current subtree
    print(data[rootPointer])

addItem("Glenn")
addItem("Sam")
addItem("Sophie")
addItem("Adam")
addItem("Saar")
addItem("Syed")

preOrderTraversal(rootPointer)

print("Removing Syed...")
removeItem("Syed")

preOrderTraversal(rootPointer)

    
    
    

