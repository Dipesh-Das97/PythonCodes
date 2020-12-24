thistuple = tuple(("apple", True, "apple"))
print(thistuple)
fruits = ("apple", "banana", "cherry", "orange", "kiwi")
print(fruits)

# unpacking tuples:
newfruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *yellow, red) = newfruits
print(green)
print(yellow)
print(red)

# type casting is very important for updating tuples
mylist = ["fruits", 'veggies', 'stationary']
mytuple = tuple(mylist) * 2
print(mytuple)
