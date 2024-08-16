def towerOfHanoi(start, end, n):
    if n == 1:
        print(f"disc 1: {start} --> {end}")
        return
    
    other = 6 - (start + end)
    
    towerOfHanoi(start, other, n-1)
    print(f"disc {n}: {start} --> {end}")
    towerOfHanoi(other, end, n-1)

towerOfHanoi(1, 3, 4)
