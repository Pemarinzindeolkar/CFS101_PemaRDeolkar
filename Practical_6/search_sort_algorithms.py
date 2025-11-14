import math
import time
import random

def linear_search_all(arr, target):
    indices = []
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            indices.append(i)
    return indices, comparisons

def binary_search_insertion_point(arr, target):
    left, right = 0, len(arr)
    comparisons = 0
    while left < right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left, comparisons

def binary_search_with_comparisons(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    comparisons = 0
    while prev < n and arr[min(step, n) - 1] < target:
        comparisons += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1, comparisons
    while prev < min(step, n):
        comparisons += 1
        if arr[prev] == target:
            return prev, comparisons
        prev += 1
    return -1, comparisons

def compare_search_algorithms(arr, target):
    print(f"\nSearching for: {target}")
    start_time = time.time()
    linear_indices, linear_comparisons = linear_search_all(arr, target)
    linear_time = time.time() - start_time
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_index, binary_comparisons = binary_search_with_comparisons(arr_sorted, target)
    binary_time = time.time() - start_time
    start_time = time.time()
    jump_index, jump_comparisons = jump_search(arr_sorted, target)
    jump_time = time.time() - start_time
    print(f"Linear Search: Indices {linear_indices}, Comparisons: {linear_comparisons}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Index {binary_index}, Comparisons: {binary_comparisons}, Time: {binary_time:.6f} seconds")
    print(f"Jump Search: Index {jump_index}, Comparisons: {jump_comparisons}, Time: {jump_time:.6f} seconds")

def main():
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    target = 5
    indices, comparisons = linear_search_all(test_list, target)
    print(f"Linear Search: Indices of {target} are {indices}, Comparisons: {comparisons}")
    test_list_sorted = sorted(test_list)
    insertion_point, comparisons = binary_search_insertion_point(test_list_sorted, target)
    print(f"Binary Search Insertion Point for {target} in sorted list: {insertion_point}, Comparisons: {comparisons}")
    index, comparisons = binary_search_with_comparisons(test_list_sorted, target)
    print(f"Binary Search: Index of {target} in sorted list is {index}, Comparisons: {comparisons}")
    index, comparisons = jump_search(test_list_sorted, target)
    print(f"Jump Search: Index of {target} in sorted list is {index}, Comparisons: {comparisons}")
    large_list = list(range(10000))
    compare_search_algorithms(large_list, 8888)
    test_list = [random.randint(1, 100) for _ in range(20)]
    target = random.choice(test_list)
    print("\nOriginal list:", test_list)
    print("Sorted list:", sorted(test_list))
    compare_search_algorithms(test_list, target)

if __name__ == "__main__":
    main()
