
#Creating a dictionary
mydict = dict(one="uno",two="des",three="tres")
mydict = {'one':"uno",'two':"des",'three':"tres"}

#Updating/ changing an element
mydict["two"] = "dos"

#Adding an element
mydict["four"] = "fres"

#Traversing a dictionary
for key in mydict:
    print(key,mydict[key])

#Searching for an element
def search(dictionary,value):
    for key in dictionary:
        if dictionary[key] == value:
            return key,value
    return "Not found"


#Deleting an element 
del mydict['four']  #Deletes the key value pair
print(mydict)

popped = mydict.pop('three')   #Returns the popped element
mydict.popitem()   #Deletes the last key, value pair of the dictionary
mydict.clear()  #Empties the dictionary

#Copying the dictionary
mydict2 = mydict.copy()

#Creating a dictionary with fromkeys method (bydefault value = None)
newdict= {}.fromkeys([1,2,3],0)  #Creates a dictionary with keys - 1,2,3 and all the valueas as 0 
print(newdict)

mydict = {'one':"uno",'two':"des",'three':"tres"}

#checking if a key value pair exists in a dictionary
print(mydict.get('uno'))

#Getting items of a dictionary
print(mydict.items())

#Getting all the keys of the dictionary
print(mydict.keys())

#Getting all the valueWrite a function to remove the duplicate numbers on given integer array/list.s of the dictionary
print(mydict.values())

#Checking if a key,value pair exists and if the key doesnt exist , it creates a key value pair with default value
mydict.setdefault("four","fres")

#Update method
mydict.update(newdict)  #Extends the newdict to mydict



