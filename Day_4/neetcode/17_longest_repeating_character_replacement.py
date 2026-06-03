def characterReplacement(s,k):
    l=0
    n=len(s)
    count=[0]*26
    longest=0
    for r in range(n):
        count[ord(s[r])-65]+=1
        while (r-l+1)-max(count)>k:
            count[ord(s[l])-65]-=1
            l+=1
        longest=max(longest,(r-l+1))
    return longest


assert characterReplacement("XYYX",2)==4
assert characterReplacement("AAABABB",1)==5
print("All cases passed")