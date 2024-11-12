numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
left = 4
right = 5
arithmetic_mean = sum(numbers[:left] + numbers[right:]) / (len(numbers[:left] + numbers[right:]) +1)
numbers[4] = round(arithmetic_mean, 2)
print("Измененный список:", numbers)
