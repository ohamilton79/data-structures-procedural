#ohamilton79
#Hash table - a procedural approach using linear probing
#28/12/2020

#CONSTANTS
MAXSIZE = 13
#Array to store hash table items
hashTableArray = [None]* MAXSIZE

#Hash function that maps the new values (keys) to array indices
def getHashVal(key, offset):
    #Get the sum of the character codes of the key, plus any offset due to linear probing
    sumOfChars = sum([ord(char) for char in key]) + offset

    #Get the modulus when divided by the size of the hash table
    hashValue = sumOfChars % MAXSIZE

    return hashValue

#Add an item to the hash table
def add(newItem, hashTableArray):
    #1. Get the hash value (array index) for the item to be added (key)
    arrayIndex = getHashVal(newItem, 0)

    #While an item already exists here, rehash (uses closed hashing)
    offset = 0
    while hashTableArray[arrayIndex] != None:
        print("Collison occured when adding '{}' - rehashing...".format(newItem))
        offset += 1
        arrayIndex = getHashVal(newItem, offset)

    #2. and 3. Add the item in this array position
    hashTableArray[arrayIndex] = newItem

#Search for an item in the hash table
def search(item, hashTableArray):
    #1. Pass the key (item being searched for) into the hash function to get the corresponding hash value
    offset = 0
    hashValue = getHashVal(item, offset)

    #2. If the value at this index isn't the one being searched for, rehash through linear probing
    while hashTableArray[hashValue] != item:
        #If the whole table is traversed, the item doesn't exist
        if offset == (MAXSIZE - 1):
            print("Item '{}' not found".format(item))
            return
        
        offset += 1
        hashValue = getHashVal(item, offset)

    #Otherwise, the item has been found at the position given by the hash value
    print("Item '{}' found at position {}".format(item, hashValue))

#Traverse each item in the linked list
def traverse(hashTableArray):
    #1. Traverse each index in the hash table array
    for i in len(hashTableArray):
        #2. Output the value stored there
        print(hashTableArray[i])

#Delete an item with a given value from the hash table
def delete(item, hashTableArray):
    #1. Pass the item to be deleted into the hash function to get the corresponding hash value
    offset = 0
    hashValue = getHashVal(item, offset)

    #2. If the value at this index isn't the one being searched for, rehash through linear probing
    while hashTableArray[hashValue] != item:
        #If the whole table is traversed, the item doesn't exist and can't be deleted
        if offset == (MAXSIZE - 1):
            print("Item '{}' can't be deleted".format(item))
            return
        
        offset += 1
        hashValue = getHashVal(item, offset)

    #Otherwise, the item can be deleted
    hashTableArray[hashValue] = None

add("Jim", hashTableArray)
print(hashTableArray)
add("Jmi", hashTableArray)
search("Jim", hashTableArray)
print(hashTableArray)
search("Natasha", hashTableArray)
print(hashTableArray)
delete("Jim", hashTableArray)
print(hashTableArray)
search("Jim", hashTableArray)
print(hashTableArray)

