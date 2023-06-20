def get_even_numbers(numbers):
    # Create an empty list to store the even numbers
    even_numbers = []

    # Iterate through the numbers in the input list
    for num in numbers:
        # Check if the number is even
        if num % 2 == 0:
            even_numbers.append(num)  # Add the even number to the list

    return even_numbers
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers) 
