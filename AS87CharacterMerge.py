#time complexity: O(n)?
word1 = input("enter first word: ") 
word2 = input("enter second word: ")
outstring = ""

bound = min(len(word1), len(word2))

for i in range(bound):
    outstring = outstring + word1[i] + word2[i]

print(outstring + word1[bound:] + word2[bound:])
