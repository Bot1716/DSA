class TelephoneBook:
    def __init__(self, name, tel_no):
        self.name = name
        self.tel_no = tel_no

#**************************************************************************************************************************
def Insertion_QuadProbing():
    hashtable = [None for _ in range(10)]
    num_records = int(input("\nEnter number of records : "))
    
    for i in range(num_records):
        n = input("Enter name : ")
        t = int(input("Enter telephone no. : "))
        hashValue = t % 10  # hash function
        j = 0  # Quadratic probing starts from j=0
        while hashtable[hashValue] is not None:  # If a collision occurs
            j += 1
            hashValue = (t % 10 + j * j) % 10  # Quadratic probing formula
        hashtable[hashValue] = TelephoneBook(n, t)  # Create and insert object into hashtable
    return hashtable

#***********************************************************************************************************************
def Insertion_DoubleHashing():
    hashtable = [None for _ in range(10)]
    num_records = int(input("\nEnter number of records : "))
    
    for i in range(num_records):
        n = input("Enter name : ")
        t = int(input("Enter telephone no. : "))
        hashvalue = t % 10  # First hash function (mod table size)
        step_size = 7 - (t % 7)  # Second hash function
        j = 0  # To control the number of probes
        while hashtable[hashvalue] is not None:  # If a collision occurs
            j += 1
            hashvalue = (hashvalue + j * step_size) % 10  # Double hashing formula
        hashtable[hashvalue] = TelephoneBook(n, t)  # Create and insert object into hashtable
    return hashtable

#***********************************************************************************************************************
def Display_QP(hash1):
    print("-------------------------------")
    print("Index\tName\tTelephone No.")
    print("-------------------------------")
    for i, obj in enumerate(hash1):
        if obj is None:
            print(f"{i}\t-\t-")
        else:
            print(f"{i}\t{obj.name}\t{obj.tel_no}")
    print("-------------------------------")

#***********************************************************************************************************************
def Display_DH(hash2):
    print("-------------------------------")
    print("Index\tName\tTelephone No.")
    print("-------------------------------")
    for i, obj in enumerate(hash2):
        if obj is None:
            print(f"{i}\t-\t-")
        else:
            print(f"{i}\t{obj.name}\t{obj.tel_no}")
    print("-------------------------------")

#***********************************************************************************************************************
def Search(hash1, hash2):
    n = input("Enter name to search: ")
    found = False
    for i, obj in enumerate(hash1):
        if obj is not None and obj.name == n:
            print("\nFound in Hashtable-1!")
            print("-------------------------------")
            print(f"Index\tName\tTelephone No.")
            print("-------------------------------")
            print(f"{i}\t{obj.name}\t{obj.tel_no}")
            print("-------------------------------")
            found = True
    for i, obj in enumerate(hash2):
        if obj is not None and obj.name == n:
            print("\nFound in Hashtable-2!")
            print("-------------------------------")
            print(f"Index\tName\tTelephone No.")
            print("-------------------------------")
            print(f"{i}\t{obj.name}\t{obj.tel_no}")
            print("-------------------------------")
            found = True
    if not found:
        print("\nNot found !!!\n")

#***********************************************************************************************************************
def main():
    # initializing hash tables to "None"
    hash1 = [None for _ in range(10)]
    hash2 = [None for _ in range(10)]
    print("-------------------------------")
    print("    Group-A Assignment-1")
    while True:
        print("-------------------------")
        print("\t1. Insert Value")
        print("\t2. Display")
        print("\t3. Search")
        print("\t4. Exit")
        print("-------------------------")
        ch = int(input("Enter choice : "))
        if ch == 1:
            print("\nSelect collision method-")
            print("\t1. Quadratic Probing")
            print("\t2. Double Hashing")
            c = int(input("Enter choice : "))
            if c == 1:
                hash1 = Insertion_QuadProbing()
            elif c == 2:
                hash2 = Insertion_DoubleHashing()
        elif ch == 2:
            print("\t1. Display QP")
            print("\t2. Display DH")
            c1 = int(input("Enter choice : "))
            if c1 == 1:
                Display_QP(hash1)  # To display hashtable which uses quadratic probing collision method
            elif c1 == 2:
                Display_DH(hash2)  # To display hashtable which uses double hashing collision method
        elif ch == 3:
            Search(hash1, hash2)
        elif ch == 4:
            quit()
        else:
            print("! Enter valid choice.")

main()

