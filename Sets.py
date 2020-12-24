set1 = {"abc", 34, True, 40, "male"}
set2 = set(set1)
print(set1)

for x in set1:
    print(x)

# Adding and Updating:
# add :
set2.add("fruits")
print("Add element : ", set2)
set2.add(("animals", "cars"))
print("Add iterables : ", set2)
# update :
set3 = set(set1)
set3.update(("animals", "cars", "male"))
print("Update : ", set3)

# Joining: union, update, intersection_union, intersection
# union
set4 = {True}
set4 = set4.union({"houses", "places", "jewels", True})
print("Union : ", set4)
# intersection_union
set4.intersection_update({"houses", True})
print("Intersection Union : ", set4)
# intersection:
set4 = set4.intersection({"houses"})
print("Intersection : ", set4)