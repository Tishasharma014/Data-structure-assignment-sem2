class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    
    # INSERT OPERATION

    def insert_begin(self, data):
        new = Node(data)

        if self.head:
            self.head.prev = new
            new.next = self.head

        self.head = new

    def insert_end(self, data):
        new = Node(data)

        if not self.head:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new
        new.prev = temp

    def insert_pos(self, pos, data):
        if pos == 0:
            self.insert_begin(data)
            return

        new = Node(data)
        temp = self.head

        for _ in range(pos - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        new.next = temp.next
        new.prev = temp

        if temp.next:
            temp.next.prev = new

        temp.next = new

    
    # DELETE OPERATIONS
    

    def delete_begin(self):
        if not self.head:
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

    def delete_end(self):
        if not self.head:
            return

        temp = self.head

        if not temp.next:
            self.head = None
            return

        while temp.next:
            temp = temp.next

        temp.prev.next = None

    def delete_value(self, key):
        temp = self.head

        while temp:
            if temp.data == key:

                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev

                return

            temp = temp.next

        print("Value not found")

    
    # SEARCH
    

    def search(self, key):
        temp = self.head
        pos = 0

        while temp:
            if temp.data == key:
                return pos
            temp = temp.next
            pos += 1

        return -1

    
    # TRAVERSAL
    

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head

        if not temp:
            return

        # go to last node
        while temp.next:
            temp = temp.next

        # traverse backward
        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.prev
        print("None")
