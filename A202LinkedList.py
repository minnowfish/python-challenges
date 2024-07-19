class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def outputList(self):
        current = self.head
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
