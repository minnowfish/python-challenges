def make_it_laugh(s):
    vowels = ["a","e","i","o","u"]
    for i in vowels:
        s= s.replace(i,"haha")
    print(s)

inputString = input("Input a string")
make_it_laugh(inputString)
