import random
wordList = ["SUBTILE","RECRUIT","DEBATED","FAVORED","DECAYED","SURPLUS","BOWLING","REGRESS","READERS","METEORS","MUFFLED","BUFFERS"]

word = random.choice(wordList)

for i in wordList:
    print(i, end="  ")

attempts = 0
while attempts < 4:
    likeless = 0
    userInput = (input("\n\n Input the password: ")).upper()
    if userInput not in wordList:
        print("not a choice")
        continue
    if userInput == word:
        print("Password Correct")
        break
    else:
        for i in range(len(word)):
            if word[i] == userInput[i]:
                likeless += 1
        print(f"Incorrect Password \n Likeless: {likeless}")
        attempts += 1
    
