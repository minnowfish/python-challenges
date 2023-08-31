#Exercise 1 Combine your skills with reading and appending to make a file that will read the existing counter.txt, count it up and then add another 10 numbers. 

counter = 0
with open("counter.txt","r") as existing_file:
    for line in existing_file:
        counter += 1
        lastnumber = int(line)
with open("counter.txt","a") as existing_file:
    for i in range(lastnumber+1, lastnumber+11):
            line_to_write = str(i)+"\n"
            existing_file.write(line_to_write)
