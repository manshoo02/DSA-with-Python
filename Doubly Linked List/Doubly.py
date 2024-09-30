class Node:
    def __init__(self,value):
        self.value =value
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1 

    def __str__(self):
        temp = self.head
        result = ""
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += " <-> "
            temp = temp.next
        return result
    
    def prepend(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    
    def traverse(self):
        temp =self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def reverse_traverse(self):
        temp = self.tail
        while temp:
            print(temp.value)
            temp = temp.prev
    
    def search(self,value):
        temp = self.head
        index = 0
        while temp:
            if temp.value == value:
                return index
            temp = temp.next
            index += 1
        return None
    
    def get(self,index):
        if index < 0  or index > self.length:
            return None
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1,index , -1):
                current = current.prev
        return current
    
    def set(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        else:
            temp = self.get(index -1)
            new_node.next = temp.next
            new_node.prev  = temp
            temp.next.prev = new_node
            temp.next = new_node
        self.length += 1

    def pop_first(self):
        popped = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped.next =None
        self.length -= 1
        return popped

    def pop(self):
        popped = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None    
        else:    
            self.tail = self.tail.prev
            self.tail.next = None
            popped.prev = None
        self.length -= 1
        return popped

    def remove(self,index):
        popped = self.get(index)
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        elif index < 0 or index >= self.length:
            return None
        else:
            popped.prev.next = popped.next
            popped.next.prev = popped.prev
            popped.prev = None
            popped.next = None
        self.length -=1 
        return popped



doubly = DLL()
doubly.append(10)
doubly.append(20)
doubly.append(30)
doubly.prepend(0)
doubly.prepend(-10)    
print(doubly)
doubly.traverse()
doubly.reverse_traverse()
print(doubly.search(30))
print(doubly.get(4).value)
doubly.set(4,40)
print(doubly)