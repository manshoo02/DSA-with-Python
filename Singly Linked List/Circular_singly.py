class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp = self.head
        result = ' '
        while temp:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += '->'
        return result

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length +=1

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
    
    def insert(self,index,value):
        new_node = Node(value)
        if index == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp = self.head
            for _ in range(index-1):
                temp =temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length -= 1

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            if temp == self.head:
                break
    
    def search(self,value):
        temp = self.head
        index = 0
        while temp:
            if temp.value == value:
                return index
            temp = temp.next
            index +=1
            if temp == self.head:
                break
    
    def get(self,index):
        current = self.head
        if index == 0:
            return self.head.value
        elif index == self.length or index  == -1:
            return self.tail.value
        elif index < 0 or index > self.length:
            return None
        else:
            for _  in range(index):
                current = current.next
            return current
    
    def set(self,index,val):
        temp = self.get(index)
        if temp:
            temp.value = val
            return True
        return False
    
    def pop_first(self):
        popped = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.tail
            popped.next = None
        self.length -= 1
        return popped
    
    def pop(self):
        popped = self.tail
        if self.length == 0:
            return None
        if self.head == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp is not self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            popped.next = None
        self.length -= 1
        return popped

    def delete_all(self):
        if self.length == 0:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length:
            return self.pop()
        else:
            prev = self.get(index -1)
            popped = prev.next
            prev.next = popped.next
            popped.next = None
        self.length -=1 
        return popped
    
    def delete_by_value(self,value):
        if self.length == 0:
            return False

        if self.head == self.tail and self.head.value == value:
            self.head = None
            self.tail = None
            self.length = 0
            return True
        
        prev = None
        current = self.head
        while True:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail =  prev

                self.length -= 1
                return True

            prev =current
            current = current.next
            if current == self.head:
                break
        return False

    def count_nodes(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
            if current == self.head:
                break     
        return count
    
    def is_sorted(self):
        if self.head is None:
            return True
        
        temp = self.head
        while temp.next != self.head:
            if temp.value > temp.next.value:
                return False
            temp = temp.next
        return True

circular = CSLL()
circular.append(0)
circular.append(10)
circular.append(20)
circular.append(30)
circular.prepend(-5)
circular.prepend(-15)
print(circular.is_sorted())
print(circular.count_nodes())
circular.insert(3,5)
circular.insert(7,35)
print(circular)
circular.traverse()
print(f"Found at  : ",circular.search(30))
print(circular.get(3).value)
circular.set(3,15)
circular.pop()
print(circular)

