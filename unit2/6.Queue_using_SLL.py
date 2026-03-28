class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None   # points to first element
        self.rear = None    # points to last element

    def enqueue(self, data):
        new = Node(data)

        if self.rear is None:
            self.front = self.rear = new
            return

        self.rear.next = new
        self.rear = new        

    def dequeue(self):
        if self.front is None:
            return "Queue Underflow"

        value = self.front.data
        self.front = self.front.next

        if self.front is None:   # queue becomes empty
            self.rear = None

        return value    
    
    def peek(self):
        return self.front.data if self.front else None
    
    def is_empty(self):
        return self.front is None
    
    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Dequeued:", q.dequeue())
q.display()

print("Front element:", q.peek())        
