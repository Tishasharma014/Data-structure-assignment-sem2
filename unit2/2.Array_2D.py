matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def row_traversal(matrix):
    count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
            count += 1   # counting each visit

        print()

    print("Total operations:", count)


# Example
row_traversal(matrix)
