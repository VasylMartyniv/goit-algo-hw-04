import random
import timeit

import pandas as pd


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def timsort(arr):
    return sorted(arr)


data_sizes = [100, 1000, 10000]
test_data = {
    size: [random.sample(range(size * 10), size) for _ in range(5)]
    for size in data_sizes
}

results = {'size': [], 'insertion_sort': [], 'merge_sort': [], 'timsort': []}
for size in data_sizes:
    for data in test_data[size]:
        results['size'].append(size)
        results['insertion_sort'].append(timeit.timeit(lambda: insertion_sort(data.copy()), number=1))
        results['merge_sort'].append(timeit.timeit(lambda: merge_sort(data.copy()), number=1))
        results['timsort'].append(timeit.timeit(lambda: timsort(data.copy()), number=1))

df = pd.DataFrame(results)
print(df)

avg_times = df.groupby('size').mean()
print(avg_times)
