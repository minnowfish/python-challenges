#Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).
wordCount = 0
totalLength = 0

with open("text.txt","r") as whole_file:
    for line in whole_file:
        words = line.split()
        wordCount += len(words)
        for w in words:
            w = '.'.join(filter(str.isalnum, w))
            totalLength += len(w)

average = totalLength/wordCount
print('The average word length is', round(average,2))
