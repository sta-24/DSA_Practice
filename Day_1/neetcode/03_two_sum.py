def two_sum(nums,target):
    seen= {}
    for i,num in enumerate(nums):
        compliment=target-num
        if compliment in seen:
            return [seen[compliment],i]
        seen[num]=i

assert two_sum([4,5,6,7],10)==[0,2]
assert two_sum([4,5,6,7],12)==[1,3]


#approach
#firsr create empty dict seen
#calculate the diff
#if diff in seen return
#else add the num as key and index as value to the dict
