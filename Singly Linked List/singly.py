class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0  
    

    def __str__(self): 
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
               result += ' -> '
            temp_node = temp_node.next
        return result


    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index ,value):
        new_node = Node(value)
        if index <0 or index > self.length:
            return False
        if index == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            
    
    def search(self,target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self,index):
        if index == -1:
            return self.tail.value
        if index <-1 or index >= self.length:
            return False
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        popped = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped.next = None
        self.length -= 1
        return popped
    
    def pop(self):
        popped = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail =temp
            temp.next = None
        self.length -= 1
        return popped.value
    
    def remove(self,index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index-1)
        popped = prev.next
        prev.next = popped.next
        popped.next =None
        self.length -=1
        return popped.value
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def reverse(self):
        prev = None
        current  = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head , self.tail = self.tail, self.head
    
    def remove_duplicates(self):
        if self.head is None:
            return
        node_values = set()  # set to store unique node values
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node

        



new_LL = SLL()
new_LL.append(10)
new_LL.append(20)
new_LL.append(40)
new_LL.insert(2,30)
print(new_LL)
print(new_LL.traverse())
print(new_LL.search(30))
print(new_LL.get(-1))
print(new_LL.remove(1))
new_LL.reverse()
print(new_LL.pop())
print(new_LL)


