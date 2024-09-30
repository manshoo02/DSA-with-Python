#LIST
l1 = [1,2,3,4,5,6]

#Accessing elements
print(l1[2])

#Traversing
for i in l1:
    print(i)

#Updating a list
l1[2] = 6
print(l1)

#Inserting a element in a list
l1.insert(2,3)
print(l1)

#Appending a list
l1.append(7)
print(l1)

#Extending a list
l2 = [8,9,10]
l1.extend(l2)
print(l1)

#Slicing a list
print(l1[0:3])

#Popping an element - when u want to know the value to be deleted
print(l1.pop(3))

#Deleting an element 
del l1[7:11]
print(l1)

#Removing an element without the index
l1.remove(6)
print(l1)

#Searching with the help of "in" operator
l3 = ['a','b','c','d']
print('a' in l3)

#Linear search
def linear(list,target):
    for i,value in enumerate(list):
        if value == target:
            return 'Found at ' + str(i)
    return 'Not found'

print(linear(l1,8))    

# "+" Opeartor in list
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

# "*" Operator in list
a = a * 3
print(a)

print(len(c))  #Length of list
print(sum(c))  #Sum of elements of the list
print(min(c))  #Min in a list
print(max(c))  #Max in a list
print(sum(c)/len(c))  #Avg

#Average of a list - function
"""
l4 = []
total = 0 
count = 0
while not False:
    value = input("Enter the number :")
    if value == "done":
        break
    value = int(value)
    count += 1
    total += value
    l4.append(value)
    
print(total/count)
print(l4)
"""

#String to a list
x = "spam"
y = list(x)
print(y)

#Split function
s = "spam1-spam2-spam3"
s=s.split("-")
print(s)

#List comprehension
a = [1,2,3]
new_a = [i**2 for i in a]
print(new_a)

#Conditional list comprehension
d = [-10,0,90,70,40,-2,-7,10]
print(d)
d = [i**2 for i in d if i<0]
print(d)