# Creating a set with curly braces
set1 = {1, 2, 3, 4, 5}

# Creating a set with the set() function
set2 = set([3, 4, 5, 6, 7])

print("Set 1:", set1)
print("Set 2:", set2)

set1.add(6)
print("After adding 6:", set1)

set1.remove(6)   # Raises an error if 6 is not found
set1.discard(5)  # Does not raise an error if 5 is not found
print("After removing elements:", set1)


union_set = set1.union(set2)
print("Union:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

difference_set = set1.difference(set2)
print("Difference:", difference_set)

symmetric_diff = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_diff)

# Clearing all elements in a set
set1.clear()
print("After clearing set1:", set1)

# Checking if an element is in a set
print(3 in set2)  # Returns True if 3 is in set2, otherwise False

subset_check = set1.issubset(set2)
superset_check = set1.issuperset(set2)
print("Is set1 a subset of set2?", subset_check)
print("Is set1 a superset of set2?", superset_check
