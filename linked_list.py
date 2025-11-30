class node:
    """
    Object that models a single node in a linked list with data and pointer to next node attributes
    """
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Data: {self.data}>"


    
class LinkedList:
    """
    The actual linkelist object
    """
    def __init__(self):
        """
        Start of the list.
        """
        self.head = None

    def is_empty(self):
        """
        Boolean if list is empty.
        """
        return self.head == None
    
    def size(self):
        """
        Counts # elements in a list starting with the head.
        """
        current = self.head
        count = 0

        while current:
            count +=1
            current = current.next_node

        return count
    

    def add(self, data):
        """
        Prepends a list.
        """
        new_node = node(data) #create a new node obj
        new_node.next_node = self.head
        self.head = new_node

    def search(self, target):
        '''
        Finds target value in a list.
        '''
        current = self.head
        while current:
            if current.data == target:
                return current
            else:
                current = current.next_node
        return None
    
    def insert (self, data, idx):
        '''
        Inserts a node with data at index.
        '''
        if idx == 0:
            self.add(data)

        elif idx > 0:
            new_node = node(data)
            current = self.head
            
            while idx > 1: #traverses up to index 1
                current = current.next_node
                idx -= 1
            
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, target):
        '''
        Removes first encountered node with target value.
        '''
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == target and current == self.head:
                found = True
                self.head == current.next_node
            elif current.data == target:
                found = True
                previous.next_node = current.next_node #jump over
            else:
                previous = current
                current = current.next_node


    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node

        return "-> ".join(nodes)

l = LinkedList()
for i in range(10):
    l.add(i)

print(l)
print(l.size())
l.insert(999, 5)
print(l)
print(l.size())
l.remove(999)
print(l)
