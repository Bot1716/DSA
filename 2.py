#with comparison
class HashTable:
    def __init__(self, size=10):
        """Initialize the hash table with the given size."""
        self.size = size
        # Initialize the table with empty lists for each bucket
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """Hash function to compute the index for a given key."""
        return hash(key) % self.size

    def insert(self, key, value, replace=False):
        """Insert key-value pair into the hash table.
        If 'replace' is True, replace the value if the key already exists."""
        index = self._hash(key)
        bucket = self.table[index]
        
        # Check if the key already exists in the bucket
        for i, (k, v) in enumerate(bucket):
            if k == key:
                if replace:
                    # Replace the value if replace is True
                    bucket[i] = (key, value)
                return
        
        # If the key doesn't exist, append the new key-value pair
        bucket.append((key, value))

    def find(self, key):
        """Find the value associated with the key."""
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v  # Return the value if the key is found
        
        return None  # If key is not found

    def delete(self, key):
        """Delete the key-value pair from the hash table."""
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]  # Delete the key-value pair
                return True  # Return True if deletion is successful
        
        return False  # Return False if key is not found

    def __str__(self):
        """Return a string representation of the hash table for debugging."""
        return str(self.table)


# Main program to accept user input and perform operations
def main():
    ht = HashTable(size=10)  # Create an instance of the hash table
    while True:
        print("\nEnter your choice:")
        print("1. Insert a key-value pair")
        print("2. Find the value associated with a key")
        print("3. Delete a key-value pair")
        print("4. Display the hash table")
        print("5. Exit")

        choice = int(input("Enter choice (1/2/3/4/5): "))
        
        if choice == 1:
            # Insert operation
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            replace = input("Replace existing value if key exists? (y/n): ").lower() == 'y'
            ht.insert(key, value, replace)
        
        elif choice == 2:
            # Find operation
            key = input("Enter the key to find: ")
            result = ht.find(key)
            if result is not None:
                print(f"The value for key '{key}' is: {result}")
            else:
                print(f"Key '{key}' not found.")
        
        elif choice == 3:
            # Delete operation
            key = input("Enter the key to delete: ")
            if ht.delete(key):
                print(f"Key '{key}' deleted successfully.")
            else:
                print(f"Key '{key}' not found.")
        
        elif choice == 4:
            # Display the hash table
            print("\nCurrent Hash Table:")
            print(ht)
        
        elif choice == 5:
            # Exit
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
