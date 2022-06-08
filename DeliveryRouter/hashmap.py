# Class for Hash Map
class HashMap(object):

    def __init__(self, size):
        # Initialize empty array of desired size
        self.size = size
        self.map = [None] * self.size
    
    # Return set size of hashMap
    def getSize(self):
        return self.size

    # Hash function for hash map to hash key modulo length to keep size ix within size
    def hash(self, key):
        size = len(self.map)
        return hash(key) % size

    ###############################
    # Linear Time Complexity O(n) #
    ###############################

    # Function to add data to hash map or update data
    def update(self, key, val):
        ix = self.hash(key)
        # Check for value within hash map.
        if self.map[ix] is not None:
            # Every key value pair within map at index ix 
            for pair in self.map[ix]:
                # If key is found and data does not match, update to new value
                if pair[0] == key:
                    pair[1] = val
                    break
            # Key not found in prior for loop so key value pair can be appended
            else:
                self.map[ix].append([key, val])
        # If map is empty, initialize one and add key value pair
        else:
            self.map[ix] = []
            self.map[ix].append([key, val])


    ###############################
    # Linear Time Complexity O(n) #
    ###############################

    # Search key in map to get value
    def get(self, key):
        ix = self.hash(key)
        if self.map[ix] is None:
            raise KeyError()
        else:
            # Search array for key and return key value pair
            for pair in self.map[ix]:
                if pair[0] == key:
                    return pair[1] 
            # Key does not exist
            raise KeyError()
