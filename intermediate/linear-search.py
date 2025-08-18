
# create a function
def linearSearch(lst, target) -> int:
    try:
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")
        if len(lst) == 0:
            raise ValueError("List is empty")

        for i, value in enumerate(lst):
            if value == target:
                return i
        return -1

    except Exception as e:
        print(f"Error: {e}")
        return -1


# create a list
lst = [11, 22, 33, 44, 55, 66, 77, 88, 99]

# create a target number
target = 55

# call the function to check
try:
    result = linearSearch(lst, target)

    if result != -1:
        print(f"The target was found at index: {result}")
    else:
        print("The target was not found")
except Exception as e:
    print(f"Unexpected error: {e}")
