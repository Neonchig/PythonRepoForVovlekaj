# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# downstairs = numbers[:6]
# upstairs = numbers[6:]

# even_els = numbers[::2]

# numbers = numbers[1:-1]

# print(downstairs, upstairs, even_els, numbers, sep = "\n")

# count_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(count_to_ten[-2::-3])

# springy_string = "Springy"

# print(springy_string[1::2])

# some_list = list(range(10))

# print(some_list[:len(some_list) // 2], some_list[(len(some_list) // 2):], sep = "\n")

nums = [-1, 3, -16, 2, 14, -22, 18]
print(nums)

print(sorted(nums, key= abs)) # сортировка по функции key

print(list(filter(lambda x: x > 0, nums))) # фильтр по функции

print(list(map(lambda x: x**2, nums))) # применение функции ко всем элементам списка