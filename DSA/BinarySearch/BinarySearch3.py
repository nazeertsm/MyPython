#**Checking of Square Root of x using Binary Search Approach**
## Method Definition
def sqrt(inp):
    right =inp
    left= 0
    result= 0
    while (left <= right):
        mid= (left+right)//2
        
        if mid*mid== inp :
            result= mid
            break
            
        elif mid*mid < inp:
            left= mid+1
            result= mid   
        else:
            right= mid -1   
    return result
# Driver Code
inp= 10
print(sqrt(inp))