class Node:
    def __init__(self,value):
        self.prev = None
        self.value = value
        self.next =None

class CDLL:
    def __init__(self):
        self.head =None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        result = " "
        while current:
            result += str(current.value)
            current = current.next
            if current.next == self.head:
                break
            result += " <-> "
        return result

    def append(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node            
            new_node.prev = self.tail
            new_node.next =self.head
            self.tail = new_node
        self.length += 1
    
    def prepend(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node            
            new_node.next = self.head
            new_node.prev = self.tail
            self.head = new_node
        self.length += 1

    def traverse(self):
        temp = self.head
        while temp.next != self.head:
            print(temp.value)
            temp = temp.next
    
    def reverse_traverse(self):
        temp = self.tail
        while temp:
            print(temp.value)
            temp = temp.prev
            if temp == self.head:
                break

    def search(self,value):
        temp = self.head
        index = 0
        while temp.next != self.head:
            if temp.value == value:
                return index
            temp = temp.next
            index += 1
        return False

    def get(self,index):
        temp = None
        if index < self.length // 2:
            temp = self.head
            for i in range(index):
                temp = temp.next
        else:
            temp = self.tail 
            for i in range(self.length - 1, index , -1):
                temp = temp.prev
        return temp

    def set(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        new_node = Node(value)
        if index == 0:
            return self.prepend()
        elif index == self.length:
            return self.append()
        elif index < 0 or index > self.length:
            return None
        else:
            temp = self.get(index -1)
            new_node.next = temp.next
            new_node.prev = temp
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
            popped.next = None
            popped.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail
            self.head = self.head.next
        self.length -= 1
        return popped

    def pop(self):
        popped = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            popped.next = None
            popped.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -= 1
        return popped

    def remove(self,index):
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            popped = self.get(index)
            popped.prev.next = popped.next
            popped.next.prev = popped.prev
            popped.next = None
            popped.prev = None
        self.length -=1 
        return popped
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        



cdoubly = CDLL()
cdoubly.append(10)
cdoubly.append(20)
cdoubly.append(30)
cdoubly.prepend(0)
cdoubly.prepend(-10)
print(cdoubly)
#cdoubly.traverse()
cdoubly.reverse_traverse()
print(cdoubly.search(20))