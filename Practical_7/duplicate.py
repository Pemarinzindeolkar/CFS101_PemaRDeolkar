def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


nums = [1, 2, 3, 4, 2]

if containsDuplicate(nums):
    print("The array contains duplicates.")
else:
    print("The array does not contain duplicates.")