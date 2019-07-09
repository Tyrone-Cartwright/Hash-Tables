

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum size
        self.count = 0  # Current size being used
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381  # arbitrary number to initialize

    for i in string:
        hash = ((hash << 5) + hash) + ord(i)

    return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    new_hash = hash(key, hash_table.capacity)

    if hash_table.storage[new_hash] and hash_table.storage[new_hash][0] != key:
        print(f"WARNING: OVERWRITING VALUE!!")

    hash_table.storage[new_hash] = (key, value)

    return

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''


def hash_table_remove(hash_table, key):
    new_hash = hash(key, hash_table.capacity)

    if not hash_table.storage[new_hash]:
        return print(f"Key {key} not found.")

    hash_table.storage[new_hash] = None

    return

# '''
# Fill this in.

# Should return None if the key is not found.
# '''


def hash_table_retrieve(hash_table, key):
    new_hash = hash(key, hash_table.capacity)

    retr = hash_table.storage[new_hash]

    if retr:
        return retr[1]
    else:
        return retr

    return


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
