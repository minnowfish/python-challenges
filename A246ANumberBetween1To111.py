def binary_search(n):
    found = False
    guesses = 0

    left, right, mid = 0, 110, 0

    while left <= right:
        guesses += 1
        mid = (right + left) // 2

        if search_array[mid] < n:
            left = mid + 1
        elif search_array[mid] > n:
            right = mid - 1
        else:
            print(f"Your number is {mid + 1} found in {guesses} guesses")
            break
        



search_array = [i for i in range(1, 112)]
number = int(input("Input your number: "))
binary_search(number)
