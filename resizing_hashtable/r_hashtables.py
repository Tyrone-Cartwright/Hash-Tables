

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.count = 0


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381  # arbitrary number to initialize

    for i in string:
        hash = ((hash << 5) + hash) + ord(i)

    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hash_key = hash(key, len(hash_table.storage))

    temp = hash_table.storage[hash_key]
    end = None

    while temp is not None and temp.key != key:
        end = temp
        temp = end.next

    new_pair = LinkedPair(key, value)
    new_pair.next = hash_table.storage[hash_key]
    hash_table.storage[hash_key] = new_pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hash_key = hash(key, len(hash_table.storage))

    temp = hash_table.storage[hash_key]
    end = None

    while temp is not None and temp.key != key:
        end = temp
        temp = end.next

    if temp is None:
        print('WARNING, value not present')
    else:
        if end is None:
            hash_table.storage[hash_key] = temp.next
        else:
            end.next = temp.next


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    hash_key = hash(key, len(hash_table.storage))

    temp = hash_table.storage[hash_key]

    while temp is not None:
        if temp.key == key:
            return temp.value
        else:
            temp = temp.next


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
