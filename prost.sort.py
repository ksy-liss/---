def bubble_sort(arr):
    n = len(arr)
    # проходим по всем элементам массива
    for i in range(n - 1):
        # флаг - были ли перестановки на текущем проходе
        swaps_occurred = False
        for j in range(n - i - 1):
            # если текущий элемент больше след. - меняем местами
            if arr[i] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # устанавливаем флаг, если была перестановка
                swaps_occurred = True
        if not swaps_occurred:
            break
    return arr

