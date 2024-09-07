#Object orientated linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def outputList(self):
        current = None
        for i in range(self.size):
            print(current.data)
            current = current.next

    def add(self, data, index):
        if index > self.size:
            return

        current = self.head
        new_node = Node(data)

        if index == 0:
            new_node.next = current
            self.head = new_node
        else:
            for i in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def find(self, data):
        current = self.head
        index = 0

        while current is not None:
            if current.data == data:
                print(f"found at {index}")
                return
            current = current.next
            index += 1
        print("not found")

    def delete(self, index):
        if index < 0 or index >= self.size:
            return

        current = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for i in range(0, index - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1

myLinkedList = LinkedList()

while True:
    print('''
    1. add
    2. find
    3. delete
    4. print list
    5. exit
    ''')
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            data = input("data : ")
            index = int(input("index : "))
            myLinkedList.add(data, index)
        case 2:
            data = input("data :")
            myLinkedList.find(data)
        case 3:
            index = int(input("index: "))
            myLinkedList.delete(index)
        case 4:
            myLinkedList.outputList()
        case 5:
            break
        case _:
            print("Invalid choice, please try again.")


#Array based linked list
def insert(letter):
   global startPointer
   global freePointer

   if freePointer == -1:
       print("Not enough space")

   else:
       next_free = alphabetList[freePointer][1]
       current = startPointer

       while letter > alphabetList[current][0] and current != -1:
           prev = current
           current = alphabetList[current][1]

       if current == startPointer:
           alphabetList[freePointer] = [letter, current]
           startPointer = freePointer
       else:
           alphabetList[freePointer] = [letter, alphabetList[prev][1]]
           alphabetList[prev][1] = freePointer

       freePointer = next_free

def delete(letter) -> bool:
   global startPointer
   global freePointer

   if startPointer == -1:
       print("The list is empty")
       return False

   current = startPointer
   while letter > alphabetList[current][0] and current != -1:
       prev = current
       current = alphabetList[current][1]

   if letter == alphabetList[current][0]:
       if current == startPointer:
           alphabetList[current][1]
       else:
           alphabetList[prev][1] = alphabetList[current][1]
       alphabetList[current][0] = ""
       alphabetList[current][1] = freePointer
       freePointer = current
       return True
   return False

alphabetList = [['e', 4], ['', 5], ['c', 0], ['b', 2], ['f', -1], ['', 6], ['', 7], ['', 8], ['', 9], ['', -1]] #array 10, 10 element char, int
startPointer = 3 #integer
freePointer = 1 #integer

for i in range(5):
   letter = input("Input letter: ")
   choice = input("Insert or Delete? ")

   if choice.title() == "Insert":
       insert(letter)
   elif choice.title() == "Delete":
       if not delete(letter):
           print("Letter not in list")

current = startPointer
while current != -1:
   print(alphabetList[current][0], end=" ")
   current = alphabetList[current][1]

