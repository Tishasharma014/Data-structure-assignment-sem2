def linear_search(arr, key):
    count = 0   # operation counter

    for i in range(len(arr)):
        count += 1   # counting comparison
        if arr[i] == key:
            print("Element found at index", i)
            print("Total operations:", count)
            return

    print("Element not found")
    print("Total operations:", count)


# Example
arr = [10, 20, 30, 40, 50]
linear_search(arr, 30)
