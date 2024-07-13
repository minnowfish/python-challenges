import datetime
from time import sleep


def timed_proc():
    userInput = None
    sentence = "the lazy fox jumped over the brown dog"
    print("lets see how long it takes for you to type the following sentence correctly")
    print(sentence)
    print("ensure the capitalisation and formatting is the SAME as the original sentence!")

    sleep(5)

    print("starting in")
    for i in range(3, 0, -1):
        print(i)
        sleep(0.5)

    start_time = datetime.datetime.now()
    while userInput != sentence:
        userInput = input("")

    return start_time

start_time = timed_proc()
time_taken = datetime.datetime.now()-start_time 
print(f"your time is {time_taken}!")
