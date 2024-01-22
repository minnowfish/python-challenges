from collections import defaultdict
def analyseText(text):
    count = defaultdict(int)

    for i in text:
        count[i] += 1
    
    sortedCount = sorted(count.items(), key=lambda x: x[1])

    mostCommon = sortedCount[-3:]
    leastCommon = sortedCount[:3]

    return mostCommon, leastCommon


text = input("Input Text: ")
text = text.lower()

mostCommon, leastCommon = analyseText(text)

print("\nTop 3 most occurring letters:")
for letter, count in mostCommon:
    print(f"{letter} with {count} occurrences")

print("\nTop 3 least occurring letters:")
for letter, count in leastCommon:
    print(f"{letter} with {count} occurrences")
