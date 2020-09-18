class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.first = None

    def add(self,value):
        if not self.first:
            self.first = Node(value)
            return True
        else:
            current = self.first
            while current.next:
                current = current.next
            current.next = Node(value)
            return True
        return False

    def delete(self):
        if not self.first:
            return False
        else:
            current = self.first
            self.first = self.first.next
            return True
        return False

    def getFirst(self):
        print(self.first.value)

    def getLast(self):
        current = self.first
        while(current.next):
            current = current.next
        print(current.value)

    def printLL(self):
        List = ""
        current = self.first
        while(current):
            List = "%s%s%s" % (List,"-->",current.value)
            current = current.next
        List = "%s%s" % (List, "-->null")
        print(List)

Books = LinkedListQueue()

Books.add("El Principito")
Books.add("Hola Mundo")
Books.add("Adios Mundo")

Books.printLL()
Books.getFirst()

Books.delete()

Books.getLast()
Books.printLL()