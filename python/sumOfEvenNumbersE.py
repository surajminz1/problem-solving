# Strings:
# Write a function that takes a list of numbers and returns the sum of all even numbers in the list.

def sum_even_numbers(numbers):
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    return sum

def main():
    # Example usage:
    numbers = [1, 2, 3, 4, 5, 6]
    even_sum = sum_even_numbers(numbers)
    print(f"The sum of even numbers is: {even_sum}")

if __name__ == "__main__":
    main()