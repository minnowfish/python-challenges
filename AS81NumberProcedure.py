def sum(numbers):
    total = 0
    for i in numbers:
        total += i

    print(f"Sum of all numbers is: {total}")

numbers = [int(x) for x in input("Input numbers separated by space: ").split()]
sum(numbers)
