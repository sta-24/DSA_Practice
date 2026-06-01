def longest_consecutive(nums):
    numset=set(nums)
    nums.sort
    longest=0

    for num in numset:
        if num-1 not in numset:
            length=0
            while num+length in numset:
                length+=1
                longest=max(length,longest)
    return longest



assert longest_consecutive([2,20,4,10,3,4,5])==4
assert longest_consecutive([0,3,2,5,4,6,1,1])==7
print("All cases pass")