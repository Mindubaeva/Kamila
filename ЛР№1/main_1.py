numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
number_copy = numbers[:]
numbers[4:5] = []
numbers_without_none = numbers
sum_ = sum(numbers_without_none)
count = len(number_copy)
average = sum_ / count
number_copy[4:5] = [average]
print("Измененный список:", number_copy)
