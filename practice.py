def sort_numbers(numbers_random):
    for i in range(len(numbers_random)):
        for z in range(len(numbers_random) - i - 1):
            if numbers_random[z] > numbers_random[z + 1]:
                numbers_random[z], numbers_random[z + 1] = numbers_random[z + 1], numbers_random[z]
    return numbers_random

def numb_search(numbers, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if numbers[middle] < element and numbers[middle + 1] >= element:
        return middle
    elif element < numbers[middle]:
        return numb_search(numbers, element, left, middle - 1)
    else:
        return numb_search(numbers, element, middle + 1, right)

try:
    numbers_random = input("Введите последовательность чисел через пробел: \n").split()
    numbers_random = list(map(int, numbers_random))
    number = int(input("Введите число: "))
except:
    print("Введены неверные данные.")
    exit()

print("Отсортированный список:", sort_numbers(numbers_random))

if number > numbers_random[-1]:
    print("В списке нет такого элемента.")
else:
    print("Номер позиции элемента:", numb_search(numbers_random, number, 0, len(numbers_random) - 1))
