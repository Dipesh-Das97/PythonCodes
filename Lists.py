thislist = ["Kiwi", 1, True, True, ("Cats", "Dogs", "Sheep")]
print(thislist)
#Constructor of list from class
newlist = list(thislist)
for x in newlist:
    print(x, " ", type(x))

fruits = list(["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"])
#Access list elements
print(fruits[0:3])
print(fruits[2:-1])
print(fruits[2:-5])
print(fruits[-5:-1])
print(fruits[:-1])
print(fruits[2:])
print(fruits[:-2])

#Check item exits in list
for x in fruits:
    if x in fruits:
        print(x)

#List Comprehension
newfruits = [x for x in fruits if 'a' in x]
print("List Comprehension: ", newfruits)
insertfruits = list(newfruits)
extendfruits = list(insertfruits)

#Adding new elements: append, insert, extend
# Append
newfruits.append("jack fruit")
print("Append : ", newfruits)
newfruits.append(thislist)
print("Append : ", newfruits)

# Insert
print("Insert : ", insertfruits)
insertfruits.insert(len(insertfruits), "strawberry")
print("Insert : ", insertfruits)
insertfruits.insert(-1, ["guava", "plum"])
print("Insert : ", insertfruits)

# Extend
print("Extend : ", extendfruits)
#extendfruits.extend("plum")
extendfruits.extend(["blueberry", "kiwi"])
print("Extend : ", extendfruits)

#Removing items: remove, pop
# Remove:
extendfruits.remove("mango")
print("Remove : ", extendfruits)
extendfruits.remove(extendfruits[4])
print("Remove : ", extendfruits)

# Pop:
extendfruits.pop(2)
print("Pop : ", extendfruits)

# Delete:
del extendfruits[1]
print("Delete : ", extendfruits)

#Sorting : sort, remove
# Sort
numbers = [50, 65, 23, 75, 100]
print("UnSorted : ", numbers)
numbers.sort()
print("Sorted : ", numbers)
numbers.sort(reverse=True)
print("Sorted in Reverse: ", numbers)


def myfunc(n):
  return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Reverse :
thislist.reverse()
print(thislist)

#Joining list: +, extend, insert, append
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
