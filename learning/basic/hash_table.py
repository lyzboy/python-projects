class HashTable:
    """Creates a simplified hash table"""
    def __init__(self):
        self.collection = dict()
    
    def hash(self, value:str)->str:
        """Creates a hash value"""
        return sum([ord(letter) for letter in value])
    
    def add(self, key:str, value:any):
        """Adds a key/value to the hash table"""
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            self.collection[hashed_key][key] = value
        else:
            self.collection[hashed_key] = {key: value}

    def remove(self, key:str)->None:
        """Removes a key/value from the hash table"""
        hashed_key = self.hash(key)
        try:
            if hashed_key in self.collection:
                del self.collection[hashed_key][key]
                if not self.collection[hashed_key]:
                    del self.collection[hashed_key]
        except KeyError:
            pass

    def lookup(self, key:str)->dict | None:
        """Returns the value of the provided key"""
        hashed_key = self.hash(key)
        try:
            if hashed_key in self.collection:
                return self.collection[hashed_key][key]
        except KeyError:
            return None

    def __str__(self):
        return_string = ""
        for hash_key, value in self.collection.items():
            return_string += f"Key: {hash_key}\nValue: {value}\n"
        return return_string

if __name__ == "__main__":
    test_table = HashTable()
    test_table.add('golf', 'club')
    test_table.add('american football', 'football')
    test_table.add('swimming', 'water')
    print(test_table)
    test_table.remove('golf')
    print(test_table)
    print(test_table.lookup('golf'))
