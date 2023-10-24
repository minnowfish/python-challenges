def ANDGate(a,b):
    return not(not (a and b) and 1)
          
def ORGate(a,b):
     return(not(not(a and 1)and not(b and 1)))

def NOTGate(a):
      return(not(a and 1))

def NORGate(a,b):
      return(not(not(not(a and 1)and not(b and 1)))and 1)

def XORGate(a,b):
      return(not(not(a and not(a and b)) and not(b and not(a and b))))
      
      
      
testData = [[1,1],[1,0],[0,1],[0,0]]
print("AND Gate:")
for i in testData:
        binary1 = i[0]
        binary2 = i[1]
        if ANDGate(binary1,binary2):
              print(f"Test Data {i} returns 1")
        else:
              print(f"Test Data {i} returns 0")

print("OR Gate")
for i in testData:
        binary1 = i[0]
        binary2 = i[1]
        if ORGate(binary1,binary2):
              print(f"Test Data {i} returns 1")
        else:
              print(f"Test Data {i} returns 0")

print("\nNOT Gate")
for i in testData:
        binary1 = i[0]
        binary2 = i[1]
        if NOTGate(binary1):
              print(f"Test Data {i[0]} returns 1")
        else:
              print(f"Test Data {i[0]} returns 0")

print("\nNOR Gate")  
for i in testData:
        binary1 = i[0]
        binary2 = i[1]
        if NORGate(binary1,binary2):
              print(f"Test Data {i} returns 1")
        else:
              print(f"Test Data {i} returns 0")

print("\nXOR Gate")
for i in testData:
        binary1 = i[0]
        binary2 = i[1]
        if XORGate(binary1,binary2):
              print(f"Test Data {i} returns 1")
        else:
              print(f"Test Data {i} returns 0")
