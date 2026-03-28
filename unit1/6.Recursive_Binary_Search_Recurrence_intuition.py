def binary_search(arr, low, high, key):
    if low > high:
        return -1   # element not found

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)


# Example
arr = [10, 20, 30, 40, 50]
key = 30

result = binary_search(arr, 0, len(arr)-1, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
