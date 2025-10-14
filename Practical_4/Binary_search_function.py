# Binary search with step-by-step tracing

def binary_search_trace(arr, target):
    left = 0
    right = len(arr) - 1
    step = 1
    while left <= right:
        mid = (left + right) // 2
        # Print the current step and search range
        print(f"Step {step}: left={left}, right={right}, mid={mid}")
        print(f"Current subarray: {arr[left:right+1]}")
        if arr[mid] == target:
            print(f"Found {target} at index {mid} after {step} steps.")
            return mid
        elif arr[mid] < target:
            print(f"{arr[mid]} < {target}, searching right half.")
            left = mid + 1
        else:
            print(f"{arr[mid]} > {target}, searching left half.")
            right = mid - 1
        step += 1
    print(f"{target} not found after {step-1} steps.")
    return -1

# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
search_for = 13
binary_search_trace(my_list, search_for)
