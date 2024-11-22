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
