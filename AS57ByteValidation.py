validation = False
while validation == False:
    parityByte = input("Input the byte you would like to validate")
    invalid = False
    for i in parityByte:
        if i != '0' and i != '1':
            invalid = True
            break
    
    if invalid:
        print("Input BINARY VALUES")
    else:
        validation = True

ones = parityByte.count("1")
zeros = parityByte.count("2")

if ones%2 != 0 or zeros%2 != 0:
    print("Error occured, parity is not even")
else:
    print("Validation passed")
