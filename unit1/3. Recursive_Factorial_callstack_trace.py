def factorial(n):
    print(f"Calling factorial({n})")

    if n == 0 or n == 1:
        print(f"Returning 1 from factorial({n})")
        return 1

    result = n * factorial(n - 1)

    print(f"Returning {result} from factorial({n})")
    return result


# Example
num = 5
print("Final Answer:", factorial(num))
