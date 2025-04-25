# Функция сортировки выбором
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Меняем местами минимальный найденный элемент с текущим
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Пример использования функции сортировки
unsorted_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(unsorted_list)
print("Отсортированный список:", sorted_list)


# Функция бинарного поиска
def binary_search(target, arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print(f"Элемент {target} найден на позиции {mid}.")
            return
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print(f"Элемент {target} не найден в списке.")


# Пример использования бинарного поиска
binary_search(22, sorted_list)