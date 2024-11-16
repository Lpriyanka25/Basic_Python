# Function to calculate the average
def calculate_average(numbers):
    if not numbers:
        return "The list is empty, no average to calculate."
    return sum(numbers) / len(numbers)

# Input: List of numbers
numbers = [10, 20, 30, 40, 50]

# Calculate and display the average
average = calculate_average(numbers)
print(f"The average is: {average}")
