class Record():
    def __init__(self, pckgName, custName, pax, cost):
        self.pckgName = pckgName
        self.custName = custName
        self.pax = pax
        self.cost = cost
    
    def __str__(self):
        return f"""
---------------------------------------------------
Package Name:<{self.pckgName}>
Customer: {self.custName}
Pax: {self.pax}
Cost: {self.cost}
"""

records = [
    Record("The Capitol Kempinski Hotel Singapore", "Jeremy Wang", 2, 340),
    Record("ONE°15 Marina, Sentosa Cove", "Revanth Ravi", 6, 330),
    Record("Shangri-La Hotel Singapore", "Reegan Goe", 1, 350),
    Record("Andaz Singapore", "Isaac Ho", 5, 250),
    Record("Sofitel Singapore City Center", "Bryan Seow", 3, 190),
    Record("Lloyd’s Inn", "Bryan Wong", 2, 160),
    Record("The Warehouse Hotel", "Lucas Lee", 3, 150),
    Record("Resorts World Sentosa – Beach Villas", "Nicole Ngan", 7, 400),
    Record("The Fullerton Hotel", "Wu Yue Wei", 8, 300),
    Record("Raffles Singapore", "Nicole Ngan", 4, 220)
]

def get_records(attr=""):
    if attr == "":
        return records
    else:
        list = []
        for obj in records:
            list.append(obj.__getattribute__(attr))
        return list
    

def menu():
    print("""
1. Display all records
2. Sort record by Customer Name using Bubble sort
3. Sort record by Package Name using Selection sort
4. Sort record by Package Cost using Insertion sort
5. Search record by Customer Name using Linear Search and update record
6. Search record by Package Name using Binary Search and update record
7. List records range from $X to $Y. e.g $100-200
8. Sort record by pax using Heap sort
0. Exit Application
    """)

def userValidation(prompt, type, ignoreEmpty = False):
    while True:
        x = input(prompt)
        if ignoreEmpty and not x:
            return x
        if x.isdecimal() and type is int and int(x) >= 0:
            return int(x)
        if x.isprintable() and type is str:
            return x
        print(f"Invalid input. Please enter a {'non negative number ' if type == int else 'string'}")

def recordDisplay(target="All"):
    if target == "All":
        printList = get_records()
    elif isinstance(target, list):
        printList = target 
    else:
        printList = [target]
    for obj in printList:
        print(obj)


def recordBSort(recList, updateRecord = True):

    n = len(recList)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
    # Bubble the largest item to the end
        for j in range(i):
            if recList[j].custName > recList[j + 1].custName:
                # Swap the j and j+1 items
                tmp = recList[j]
                recList[j] = recList[j + 1]
                recList[j + 1] = tmp

    if updateRecord:
        records = recList
    else:
        return recList

def recordSSort(recList, updateRecord = True):
    n = len( recList )
    for i in range(n - 1):
    # Assume the ith element is the smallest.
        smallNdx = i
    # Determine if any other element contains a smaller value.
        for j in range(i+1, n):
            if recList[j].pckgName < recList[smallNdx].pckgName:
                smallNdx = j
        # Swap the ith value and smallNdx value only if the smallest
        # value is not already in its proper position.
        if smallNdx != i:
            tmp = recList[i]
            recList[i] = recList[smallNdx]
            recList[smallNdx] = tmp

    if updateRecord:
        records = recList
    else:
        return recList

def recordISort(recList, updateRecord = True):
    n = len(recList)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned
        value = recList[i]
        # Find the position where value fits in the
        # ordered part of the list.
        pos = i
        while pos > 0 and value.cost < recList[pos - 1].cost:
            # Shift the items to the right during the search
            recList[pos] = recList[pos-1]
            pos -= 1
            # Put the saved value into the open slot.
            recList[pos] = value

    if updateRecord:
        records = recList
    else:
        return recList

def recordUpdate(records):
    pckgNames = get_records("pckgName")

    if len(records) > 1:
        for index, record in enumerate(records, 1):
            print(f"""
{index}.  Package Name: {record.pckgName}
    Customer: {record.custName}
    Pax: {record.pax}
    Cost: {record.cost}""")

        while True:
            selection = userValidation(f"Which record would u like to update? (0 to return): ", int)
            if selection == 0:
                print("Returning to main menu...")
                return
            elif selection-1 < len(records):
                break
            print(f"Invalid Selection. Please select a number from 1 to {len(records)}")

        record = records[selection-1]
    else:
        record = records[0]
        recordDisplay(record)
        
    
    pckgNames.remove(record.pckgName)

    old = Record(record.pckgName, record.custName, record.pax, record.cost)
    while True:
        x = userValidation("Enter New Package Name (Leave empty unchanged):", str, True).title()
        if x not in pckgNames:
            break
        print("Package Name currently exists!")
    record.pckgName = x if x else record.pckgName
    while True:
        x = userValidation("Enter New Customer Name (Leave empty unchanged):", str, True).title()
        if not x or x.replace(" ", "").isalpha():
            break
        print("Customer Name should not contain any numbers!")
    record.custName = x if x else record.custName
    x = userValidation("Enter New number of Pax (Leave empty unchanged):", int, True)
    record.pax = x if x else record.pax
    x = userValidation("Enter New Package Cost (Leave empty unchanged):", int, True)
    record.cost = x if x else record.cost

    print(f"""
---------------------------------------------------
Package Name: {old.pckgName if old.pckgName == record.pckgName else f"<{old.pckgName}> ---> <{record.pckgName}>"}
Customer: {old.custName if old.custName == record.custName else str(old.custName) + " --- " + str(record.custName)}
Pax: {old.pax if old.pax == record.pax else str(old.pax) + " ---> " + str(record.pax)}
Cost: {old.cost if old.cost == record.cost else str(old.cost) + " ---> " + str(record.cost)}
""")

    

def recordLSearch():
    list = get_records()
    n = len(list)
    result = []
    while True:
        target = input("Enter Customer Name to search for (0 to return): ")
        if target == "0":
            return None
        for i in range(n):
            if list[i].custName.lower() == target.lower():
                result.append(list[i])
        if not result:
            print("Customer Name not found! Try again.")
        else:
            return result
    

def recordBSearch():
    while True:
        x = input("Enter Customer Name to search for (0 to return): ")
        if x == "0":
            return None
        recList = get_records()
        recordSSort(recList)

        n = len(recList)
        high = n-1
        low = 0

        while True:
            if high < low:
                print("Package Name not found! Try again.")
                break
            mid = (high+low)//2
            if recList[mid].pckgName.lower() == x.lower():
                return recList[mid]
            elif recList[mid].pckgName.lower() < x.lower():
                low = mid+1
            elif recList[mid].pckgName.lower() > x.lower():
                high = mid-1

def recordsListRange():
    while True:
        x = input("Enter a range to search for ($X-$Y): ")
        if x == "0":
            return
        elif x.find("-") == -1:
            print("Enter a valid range")
        else:
            ranges = x.split("-")
            if not (ranges[1].isdecimal() and ranges[0].isdecimal()):
                print("$X and $Y has to be a number")
            
            else:
                recList = get_records()
                recList = recordISort(recList, False)
                high = int(ranges[1])
                low = int(ranges[0])
                if low > high:
                    recList.reverse()
                    tmp = low
                    low = high
                    high = tmp

                for obj in recList:
                    if low <= obj.cost <= high: 
                        recordDisplay(obj)
                return 

def heapify(recList, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and recList[largest].pax < recList[l].pax:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and recList[largest].pax < recList[r].pax:
        largest = r
 
    # Change root, if needed
    if largest != i:
        recList[i], recList[largest] = recList[largest], recList[i]  # swap
 
        # Heapify the root.
        heapify(recList, n, largest)
 
# The main function to sort an array of given size
 
 
def recordHeapSort(recList):
    n = len(recList)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(recList, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        recList[i], recList[0] = recList[0], recList[i]  # swap
        heapify(recList, i, 0)


def main():
    x = True
    y = 0
    while True:
        if x or y==5:
            y=0
            menu()
        userInput = input("Enter a number from 1-8 to begin (0 to exit program): ")
        if userInput == "1":
            recordDisplay()
        elif userInput == "2":
            recordBSort(get_records())
            recordDisplay()
        elif userInput == "3":
            recordSSort(get_records())
            recordDisplay()
        elif userInput == "4":
            recordISort(get_records())
            recordDisplay()
        elif userInput == "5":
            result = recordLSearch()
            if result:
                recordUpdate(result)
        elif userInput == "6":
            result = recordBSearch()
            if result:
                recordUpdate([result])
        elif userInput == "7":
            recordsListRange()
        elif userInput == "8":
            recordHeapSort(get_records())
            recordDisplay()
        elif userInput == "0":
            print("Ending program...")
            exit()
        else:
            print("Invalid Option")
            x = False
            y+=1

main()