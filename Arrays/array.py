import array as ar
import numpy as np

#Creating an array and traversing through it
arr1 = ar.array('i',[1,2,3,4,5])
arr2 = ar.array('i',[8,9,10])
def traverse(array):
    for i in array:
        print(i)
traverse(arr1)

#Accessing elements of an array
def access(array,index):
    if index >= len(array):
        print("Index out of range")
    else:
        print(array[index])
access(arr1,2)

#Appending an array
arr1.append(7)

#Inserting an element on a particular location in an array
arr1.insert(5,6)

#Extending an array with another array
arr1.extend(arr2)
print(arr1)

#Adding items from list in an array with the help of fromlist() function
l1= [1,3,5,7]
arr1.fromlist(l1)
print(arr1)

#Removing last element of an array
arr1.pop()
print(arr1)

#Fetching any element's index
print(arr1.index(5))

#Reversing an array using reverse() function
arr1.reverse()
print(arr1)

#Array buffer information
print(arr1.buffer_info())

#Counting the no. of occurences of an element
print(arr1.count(5))

#Converting array to a python list
print(arr1.tolist())

#Slicing elements from an array
print(arr1[1:4])






#Creating a 2D array
twoD = np.array([[1,2,3,4],[6,7,8,9],[11,12,13,14]])
print(twoD)

#Inserting a column in a 2D array
newtowD1= np.insert(twoD, 0 ,[0,5,10], axis=1)
print(newtowD1)

#Inserting a row at the end in a 2D array
newtowD2 = np.append(newtowD1, [[15,16,17,18,19]], axis=0)
print(newtowD2)

#Accesssing elements of a 2D array
def access2D(array,row_index,column_index):
    if row_index >= len(array) or column_index >= len(array[row_index]):
        print("Incorrect index")
    else:
        print(array[row_index][column_index])

access2D(newtowD2,2,6)


#Traversing a 2D array
def traverse_2D(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverse_2D(newtowD2)


#Searching an element in a 2D rray
def search_2D(array , value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at row ' + str(i) + " and column " +str(j)
    return "Element not found"        
print(search_2D(newtowD2,19))

#Deletion from a 2D array
twoD = np.array([[1,2,3,4],[6,7,8,9],[11,12,13,14]])
new = np.delete(twoD,0,axis=0)
print(new)
new = np.delete(new,3,axis=1)
print(new)