# Empty tuple
empty_tuple = ()

# Tuple with elements
my_tuple = (1, 2, 3, "apple", "banana")

# Access first element
print(my_tuple[0])  # Output: 1

# Access last element
print(my_tuple[-1])  # Output: "banana"

a, b, c, d, e = my_tuple
print(a)  # Output: 1
print(d)  # Output: "apple"

tuple1 = (1, 2, 3)
tuple2 = (4, 5)

# Concatenation
result = tuple1 + tuple2  # Output: (1, 2, 3, 4, 5)

# Repetition
result = tuple1 * 2  # Output: (1, 2, 3, 1, 2, 3)

sample_tuple = (1, 2, 3, 2, 4)

# Count occurrences of an element
print(sample_tuple.count(2))  # Output: 2

# Find index of an element
print(sample_tuple.index(3))  # Output: 2

my_dict = {(1, 2): "point A", (3, 4): "point B"}
print(my_dict[(1, 2)])  # Output: "point A"

coordinates = (10.5, 20.3)
print("X:", coordinates[0], "Y:", coordinates[1])
