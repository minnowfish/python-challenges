#Exercise 1: Create an auto-prompter that lets you read the poem at a sensible pace. 
import time
with open("rudyard.txt","r") as whole_file:
   for line in whole_file:
        time.sleep(0)
        print(line, end="")

#Exercise 2: The female equivalent to this poem is mam.txt , create an auto-prompter that lets you choose the file that you want and auto prompts for you.
choice = int(input('''
\n Which file would you like to choose?
    1) rudyard.txt
    2) mam.txt
               '''))

if choice == 1:
    with open("rudyard.txt","r") as whole_file:
        for line in whole_file:
            time.sleep(1)
            print(line, end="")
elif choice ==2:
    with open("mam.txt","r") as whole_file:
         for line in whole_file:
            time.sleep(1)
            print(line, end="")
else:
    print("Not an option, please input 1 or 2")
