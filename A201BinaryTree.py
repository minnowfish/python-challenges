class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
            
    def find(self, value) -> bool:
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        return True
    
    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            successor = self.right
            while successor.left:
                successor = successor.left

            self.value = successor.value
            self.right = self.right.delete(successor.value)

        return self



    
tree = Node(50)
tree.insert(29)
tree.insert(13)
tree.insert(30)
tree.insert(839)
tree.insert(89)

#-----------TESTING-----------
#checking insertion
print(tree.left.value) #expect 29
print(tree.right.value) #expect 839
print(tree.left.left.value) #expect 13
print(tree.left.right.value) #expect 30
print(tree.right.left.value) #expect 89
print(tree.left.left.right, "\n") #expect None

#checking find
print(tree.find(50)) #expect True
print(tree.find(29)) #expect True
print(tree.find(1), "\n") #expect False

#checking deletion
tree.delete(30)
print(tree.left.right) #expect None

tree.delete(29)
print(tree.left.value) #expect 13

tree.delete(50)
print(tree.value) #expect 89
