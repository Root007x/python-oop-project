numbers = [1,2,3,4,4,5,6]

nums = [num for num in numbers]
nums2 = [num for num in numbers if num % 2 == 0]

print(nums2)