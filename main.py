import time
import random
import matplotlib.pyplot as plt

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort
def mergeSort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort
def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            pivot_index = partition(items, low, high)
            _quick_sort(items, low, pivot_index - 1)
            _quick_sort(items, pivot_index + 1, high)

    def partition(items, low, high):
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)

# Radix Sort
def radix_sort(arr):
    max_num = int(max(arr))
    exp = 1
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = int(arr[i]) // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = int(arr[i]) // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

# Python's built-in sort
def python_sort(arr):
    return sorted(arr)

# Testing the sorting algorithms and plotting results
def test_sorting_algorithms():
    sizes = [50, 100, 200]
    algorithms = ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Radix Sort', 'Python Sort']
    results = {algo: [] for algo in algorithms}

    for size in sizes:
        arr = [random.uniform(0.1, 100.0) for _ in range(size)]
        copies = {algo: list(arr) for algo in algorithms}

        start = time.time()
        bubble_sort(copies['Bubble Sort'])
        results['Bubble Sort'].append(time.time() - start)

        start = time.time()
        selection_sort(copies['Selection Sort'])
        results['Selection Sort'].append(time.time() - start)

        start = time.time()
        insertion_sort(copies['Insertion Sort'])
        results['Insertion Sort'].append(time.time() - start)

        start = time.time()
        mergeSort(copies['Merge Sort'])
        results['Merge Sort'].append(time.time() - start)

        start = time.time()
        quick_sort(copies['Quick Sort'])
        results['Quick Sort'].append(time.time() - start)

        start = time.time()
        radix_sort(copies['Radix Sort'])
        results['Radix Sort'].append(time.time() - start)

        start = time.time()
        python_sort(copies['Python Sort'])
        results['Python Sort'].append(time.time() - start)

    return sizes, results

sizes, results = test_sorting_algorithms()
plt.figure(figsize=(10, 6))
for algo, times in results.items():
    plt.plot(sizes, times, marker='o', label=algo)

plt.title('Sorting Algorithms Execution Time Comparison')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# bubble sort and selection sort are very slow, but selection is still slightly better
# insertion sort is better than both but not efficient for large input sizes
# merge sort is faster and efficient for large datasets
# quick sort is also very fast and often outperforms merge sort in practice for average cases
