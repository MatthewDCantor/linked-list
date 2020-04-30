class LinkedList:
        
    """ init - Initalize a linked list. Payload will be
    set to value of the link, which can later be used for searching
    """
    def __init__(self, payload):
        self.pl = payload
        self.next = None

    """ Add - create a new node and it to the list.

    The new node should be added to the front of the list.

    """
    def add(self, payload):
        #TODO: Implement this function
        

    """ Remove - Remove the node from the list that equals query 
    
    """
    def remove(self, query):
        #TODO: Implement this function

    """ Search - Search for query in the list.

    If query is found, then the item that was added to the node, if it isn't
    then False will be returned

    """
    def search(self, query):
        #TODO: Implement this function

    """ isEmpty - Return True if the list is Empty, False otherwise

    TODO: Implement this function
    """
    def isEmpty(self):
        #TODO: Implement this function


    def print_list(self):
        i=0
        cur = self.next
        while(cur.next != None):
            print(i, ":", cur.pl)
            i += 1
            cur = cur.next


def init_list():
    return LinkedList(None)
