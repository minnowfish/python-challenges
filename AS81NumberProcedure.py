def sum(numbers):
    total = 0
    product = 1
    for i in numbers:
        total += i
        product *= i

    print(f"Sum of all numbers is {total} and product is {product}")

numbers = [int(x) for x in input("Input numbers separated by space: ").split()]
sum(numbers)
