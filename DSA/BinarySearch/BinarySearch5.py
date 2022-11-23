#**Finding a perfect square**
## Method Definition
def perfect_square(num):
    
    left= 0
    right= num
    
    while left<= right:
        mid= (left+right)//2
        
        if mid*mid== num:
            return True
        
        elif mid*mid> num:
            right= mid-1
            
        else:
            left= mid+1
    return False

## Driver Code
num= 28
perfect_square(num)