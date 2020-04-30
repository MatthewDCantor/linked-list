class LinkedList:
        
    """ init - Initalize a linked list. Payload will be
    set to value of the link, which can later be used for searching
    """
    def __init__(self, payload):
        self.pl = payload
        self.next = None

    """ Add - create a new node and it to the list.

    The new node should be added to the front of the list.

    TODO: Implement this function
    """
    def add(self, payload):
        node = LinkedList(payload)
        node.next = self.next 
        self.next = node
        

    """ Remove - Remove the node from the list that equals query 
    
    TODO: Implement this function
    """
    def remove(self, query):
        cur = self.next
        prev = self

        while(cur.next != None):
            if cur.pl == query:
                prev.next = cur.next
                return True

            cur = cur.next
            prev = prev.next

        return False

    """ Search - Search for query in the list.

    If query is found, then the item that was added to the node, if it isn't
    then False will be returned

    TODO: Implement this function
    """
    def search(self, query):
        cur = self

        while(cur.next != None):

            if cur.pl == query:
                return cur.pl

            cur = cur.next
        
        return False

    """ isEmpty - Return True if the list is Empty, False otherwise

    TODO: Implement this function
    """
    def isEmpty(self):
        if self.next == None:
            return True

    def print_list(self):
        i=0
        cur = self.next
        while(cur.next != None):
            print(i, ":", cur.pl)
            i += 1
            cur = cur.next


def init_list():
    return LinkedList(None)
