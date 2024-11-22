student = {
    "name": "John",
    "age": 20,
    "course": "Computer Science"
}

# Accessing values by key
print(student["name"])  # Output: John
print(student["age"])   # Output: 20

# Using .get() to access values (avoids errors if the key is missing)
print(student.get("grade", "Not Available"))

# Adding a new key-value pair
student["grade"] = "A"
print(student)  # {'name': 'John', 'age': 20, 'course': 'Computer Science', 'grade': 'A'}

# Updating an existing key
student["age"] = 21
print(student)  # {'name': 'John', 'age': 21, 'course': 'Computer Science', 'grade': 'A'}

# Removing a key-value pair
student.pop("grade")
print(student)  # {'name': 'John', 'age': 21, 'course': 'Computer Science'}
