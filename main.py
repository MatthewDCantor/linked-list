import sys
from LinkedList.LinkedList import init_list
import random


""" generate_numbers - Generate n random integers between (lower, upper)
"""
def generate_numbers(n, lower, upper):
    nums = [None] * n

    for i in range(n):
        nums[i] = random.randint(lower, upper)

    return nums

def test_linked_list(lst, nItems):
    items = generate_numbers(nItems, 0, 100)

    lst = init_list()

    if not lst.isEmpty:
        print("ERROR: The list was not empty when it should have been")
        sys.exit(-1)

    print(items)

    
    print("Testing adding and searching ... ", end='');
    for item in items:
        lst.add(item)

    for item in items:
        result = lst.search(item)
        if result != item:
            print("FAILED")
            print("Search for:", item, "but got:", result)
            sys.exit(-1)

    print("PASSED")

    items.reverse()
    print(items)
    
    print("Checking to see if list has correct order ...", end=' ')
    i = 0
    cur = lst.next
    while(cur.next != None):
        if items[i] != cur.pl:
            print("FAILED!")
            print(i, "value was not in the right place")
            print("Expected:", items[i], "but got:", cur.pl)
            return False
    
        i += 1
        cur = cur.next
    print("PASSED!")


    print("Testing remove ...", end=' ')
    itm = item[3]
    lst.remove(item[3])
    items.remove(3)
    if not lst.search(itm):
        print("FAILED")
        print("Search returned an item that should have been removed")
        sys.exit(-1)


if __name__ == "__main__":
    random.seed(1)


    items = generate_numbers(10, 0, 10)
    lst = init_list()

    if not lst.isEmpty:
        print("The list was not empty when it should have been")
    
    for item in items:
        lst.add(item)


    # Uncomment this function call when you're ready to test
    test_linked_list(lst, 10)
    
