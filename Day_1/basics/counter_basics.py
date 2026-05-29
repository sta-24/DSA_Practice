from collections import Counter
nums=[1,1,1,2,3,3,4,4,5,4,4]
k=3

print(Counter(nums))

op=[]
for i in Counter(nums):
    if len(op)==k:
        break
    op.append(i)

print(op)
