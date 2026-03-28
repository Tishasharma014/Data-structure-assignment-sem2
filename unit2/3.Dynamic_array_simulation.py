class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.arr = self.make_array(self.capacity)

    def make_array(self, capacity):
        return [None] * capacity

    # Append (Add element)
    def append(self, value):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)

        self.arr[self.size] = value
        self.size += 1

    # Resize function
    def resize(self, new_capacity):
        print(f"Resizing from {self.capacity} to {new_capacity}")
        new_arr = self.make_array(new_capacity)

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_capacity

    # Pop (Remove last element)
    def pop(self):
        if self.size == 0:
            print("Array is empty")
            return None

        value = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1

        # Optional: shrink size when too empty
        if self.size > 0 and self.size <= self.capacity // 4:
            self.resize(self.capacity // 2)

        return value

    # Display
    def display(self):
        print([self.arr[i] for i in range(self.size)])
