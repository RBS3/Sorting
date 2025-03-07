import time
import random
def bubble_sort(arr):
    """
    Bubble Sort algorithm to  sort a list in ascending order.
    :param arr: List of numbers
    :return: Sorted list
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def selection_sort(arr):
    """
    Selection Sort algorithm to sort a list in ascending order.
    :param arr: List of numbers
    :return: Sorted list
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def test_sorting_algorithms():
    sizes = [50, 1000]
    for size in sizes:
        arr1 = [random.uniform(0.1, 100.0) for _ in range(size)]
        arr2 = list(arr1)

        start_time = time.time()
        bubble_sort(arr1)
        bubble_time = time.time() - start_time

        start_time = time.time()
        selection_sort(arr2)
        selection_time = time.time() - start_time

        print(f"Warehouse Size: {size} Products")
        print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
        print(f"Selection Sort Time: {selection_time:.6f} seconds")
        print("-" * 40)


test_sorting_algorithms()
