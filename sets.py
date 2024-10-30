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
