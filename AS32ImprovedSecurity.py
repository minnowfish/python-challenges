import random
def numberAssignment(floors):
    assignment = []
    for i in range(1,floors+1):
        assignment.append(i)
    
    random.shuffle(assignment)
    return assignment
    

floors = int(input("Input the number of floors: "))
assignment = numberAssignment(floors)
print("Floor Assignment for Guards:")
for i in assignment:
    print(i)
