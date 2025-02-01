def convert_add(lst):
    return sum(int(num) for num in lst)

# Example usage:
numbers = ["1", "3", "5"]
result = convert_add(numbers)
print(result)