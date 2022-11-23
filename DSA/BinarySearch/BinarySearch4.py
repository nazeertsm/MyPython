#**First Bad Version**
## Method Definition
def first_bad_version(a):
    left= 0
    right= len(a)-1
    ans=0
    while left <= right:
        mid= (left+right)//2
        if a[mid-1] ==0 and a[mid]==1:
            ans= mid
            break
        elif a[mid]==0:
            left= mid+1
        else:
            right= mid-1
        
    return ans

# Driver Code
inp=[0,1,1,1,1,1]
first_bad_version(inp)