thisdictionary = {
    "firstname": "Dipesh",
    "lastname": "Das",
    "age": 22,
    "graduated": False
}
print(thisdictionary)
for x in thisdictionary:
    print(x + ": ", thisdictionary[x])
# Access using methods:
key = thisdictionary.keys()
print(key)
for y in key:
    print(thisdictionary[y])

# Update:
thisdictionary.update({"completed": True})
print(thisdictionary)
thisdictionary.update({"company": "Full"})
print(thisdictionary)

# nested dictionary:
newdictionary = {
    "object1": {
        "firstname": "Dipesh",
        "lastname": "Das",
        "age": 22,
        "graduated": False
    },
    "object2": {
        "firstname": "Sahil",
        "lastname": "Das",
        "age": 15,
        "graduated": False
    }
}
print(newdictionary)

print("W/O methods : ")
for x in newdictionary:
    print(newdictionary[x])
    for y in newdictionary[x]:
        print(newdictionary[x][y])
print("W methods : ")
for x in newdictionary.keys():
    print(x)
    for y in newdictionary[x].values():
        print(y)