## Function Definition
## Code written by Gagan R
def ternarySearch(arr,i,j,key):
    ## compute the values of mid1 and mid2
    mid1 = i + (j-i)//3
    mid2 = j - (j-i)//3
    
    while i<=j:
        
        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2
        ## first part of the ternary search
        elif key < arr[mid1]:
            ## recursive call
            return ternarySearch(arr,i,mid1-1,key)
        ## third part of the ternary search
        elif key > arr[mid2]:
            ## recursive call
            return ternarySearch(arr,mid2+1,j,key)
        else:
            ## second part of the ternary search
            ## recursive call
            return ternarySearch(arr,mid1+1,mid2-1,key)
    ## if the searching element is not present in the array
    return -1
    

## Driver code ##
arr = [20,25,47,56,59,63,65,79,82]
i = 0
j = len(arr)-1
key = int(input('Enter number to be found: '))
## function calling
position = ternarySearch(arr,i,j,key)
print(position)