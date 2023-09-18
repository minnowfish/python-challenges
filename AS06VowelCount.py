vowels = ['a','e','i','o','u']
count = 0
word = input("Input a word")

for i in word:
    if i in vowels:
        count += 1

print(count)
