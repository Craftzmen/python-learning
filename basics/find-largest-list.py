
# create a function
def findLargestInList(numbers) -> int:
    try:
        if not isinstance(numbers, list):
            raise TypeError("Input must be a list")
        if len(numbers) == 0:
            raise ValueError("List is empty")

        largest = numbers[0]
        for number in numbers:
            if number > largest:
                largest = number
        return largest

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None


# create a numbers list of any range
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# check if the number is the largest
largest = findLargestInList(list_of_numbers)

# print the largest number
if largest is not None:
    print(f"Largest: {largest}")
