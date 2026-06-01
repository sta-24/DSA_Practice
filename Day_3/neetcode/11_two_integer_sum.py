def two_sum_2(numbers,target):
    left,right=0,len(numbers)-1
    while left<right:
        sum=numbers[left]+numbers[right]
        if sum==target:
            return [left+1,right+1]
        elif sum<target:
            left+=1
        else:
            right1-=1
        return []


assert two_sum_2([1,2,3,4],3)==[1,2]
print("case passed")