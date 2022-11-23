## function definition
## time complexity: O(log(m*n))
def search2DArray(arr, target):
    ## number of rows
    m = len(arr)
    if m == 0:
        return False
    ## number of columns
    n = len(arr[0])
    left, right = 0, m*n-1
    ## binary search implementation
    while left <= right:
        mid = left + (right - left)//2
        ## row_number -> mid//n
        ## column_number -> mid%n
        mid_element = arr[mid//n][mid%n]
        if target == mid_element:
            return True
        elif target < mid_element:
            right = mid - 1
        else:
            left = mid + 1
    return False


## Driver code
arr = [[1,3,5,7],[10,11,16,20], [23,30,34,60]]
target = 70
result = search2DArray(arr, target)
print(result)