#example 1
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

#example 2
def calculate_average(numbers):
    """
    Function to calculate the average of a list of numbers.
    :param numbers: List of numerical values
    :return: Average of the list or a message if the list is empty
    """
    if len(numbers) == 0:  # Check if the list is empty
        return "The list is empty, so no average can be calculated."
    return sum(numbers) / len(numbers)

# Taking input from the user
try:
    user_input = input("Enter numbers separated by spaces: ")
    # Convert input string into a list of numbers
    numbers = list(map(float, user_input.split()))
    average = calculate_average(numbers)
    print(f"The average of the entered numbers is: {average}")
except ValueError:
    print("Please enter valid numbers.")
