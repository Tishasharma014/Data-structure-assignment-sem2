def insert(arr, n, pos, value):
    count = 0   # operation counter

    arr.append(None)  # increase size

    # shift elements to right
    for i in range(n-1, pos-1, -1):
        arr[i+1] = arr[i]
        count += 1   # counting shifts

    arr[pos] = value

    print("Array after insertion:", arr)
    print("Shifting operations:", count)


# Example
arr = [10, 20, 30, 40, 50]
insert(arr, len(arr), 2, 25)
