def contains_duplicates(nums):
    return len(nums)!=len(set(nums))



assert contains_duplicates([1,2,3,4])==False
assert contains_duplicates([1,2,2,4])==True
print("All test cases passed")