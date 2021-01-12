#ohamilton79
#Hash table - a procedural approach using chaining
#28/12/2020

#Dependent on module implementing linked lists (in 'Data Structures - Procedural' repo)
import linkedListWithArrays

#CONSTANTS
MAXSIZE = 13
#Array to store linked lists containing hash table items
hashTableArray = [linkedListWithArrays.create() for i in range(MAXSIZE)]

#Hash function that maps the new values (keys) to array indices
def hash(key):
    #Get the sum of the character codes of the key
    sumOfChars = sum([ord(char) for char in key])

    #Get the modulus when divided by the size of the hash table
    hashValue = sumOfChars % MAXSIZE

    return hashValue

#Add an item to the hash table
def add(newItem, hashTableArray):
    #1. Get the hash value (array index) for the item to be added (key)
    arrayIndex = hash(newItem)

    #2. and 3. Add the item to the linked list in this array position
    listProperties = hashTableArray[arrayIndex]
    hashTableArray[arrayIndex] = linkedListWithArrays.addItem(newItem, listProperties[0], listProperties[1], listProperties[2], listProperties[3])

#Search for an item in the hash table
def search(item, hashTableArray):
    #1. Pass the key (item being searched for) into the hash function to get the corresponding hash value
    hashValue = hash(item)

    #2. Retrieve the contents at the index specified by this hash value in the hash table
    listProperties = hashTableArray[hashValue]

    #3. Search the returned linked list until the item is found
    linkedListWithArrays.search(item, listProperties[0], listProperties[1], listProperties[2], listProperties[3])

#Traverse each item in the linked list
def traverse(hashTableArray):
    #1. Traverse each position in the hash table array
    for linkedList in hashTableArray:
        #2. Traverse each linked list
        linkedListWithArrays.traverse(linkedList[0], linkedList[1], linkedList[2], linkedList[3])

#Delete an item with a given value from the hash table
def delete(item, hashTableArray):
    #1. Pass the item to be deleted into the hash function to get the corresponding hash value
    hashValue = hash(item)

    #2. Search for the item in the linked list at this location and try to delete it
    linkedList = hashTableArray[hashValue]
    itemPos = linkedListWithArrays.search(item, linkedList[0], linkedList[1], linkedList[2], linkedList[3])

    #If the item can be deleted
    if itemPos != None:
        hashTableArray[hashValue] = linkedListWithArrays.removeAt(itemPos, linkedList[0], linkedList[1], linkedList[2], linkedList[3])
    else:
        print("Item can't be deleted")

    pass

add("Jim", hashTableArray)
search("Jim", hashTableArray)
search("Natasha", hashTableArray)
delete("Jim", hashTableArray)
search("Jim", hashTableArray)

#for linkedList in hashTableArray:
#    print(linkedList[0])
#print(hashTableArray)

    
