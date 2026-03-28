# Stack implementation using Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # push operation
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    # pop operation
    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data

    # check if empty
    def is_empty(self):
        return self.top is None

    # peek operation
    def peek(self):
        if self.top is None:
            return None
        return self.top.data


# function to check balanced parentheses
def is_balanced(expression):
    s = Stack()

    for ch in expression:
        # if opening bracket, push
        if ch in "({[":
            s.push(ch)

        # if closing bracket
        elif ch in ")}]":
            if s.is_empty():
                return False

            top = s.pop()

            # matching conditions
            if (ch == ')' and top != '(') or \
               (ch == '}' and top != '{') or \
               (ch == ']' and top != '['):
                return False

    # if stack is empty at end -> balanced
    return s.is_empty()


# main part
expr = input("Enter expression: ")

if is_balanced(expr):
    print("Balanced")
else:
    print("Not Balanced")
