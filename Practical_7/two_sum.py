def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []  

nums = [2, 7, 11, 15]
target = 9

result = twoSum(nums, target)

if result:
    print(f"Indices of numbers that add up to {target}: {result}")
else:
    print("No two numbers add up to the target.")