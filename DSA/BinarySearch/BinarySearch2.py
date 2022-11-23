## Binary Search Algorithm without using recursion(iterative)
## function definition
def binarySearch(arr, x, i, j):
    while i <= j:
        ## lower bound while division
        mid = i + (j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            ## right side of the mid
            ## seach space - mid+1 to j
            i = mid + 1
            ## arr[mid] > x:
        else:
            ## left side of the mid
            ## search space - i to mid-1
            j = mid - 1
    ## searching element is not present in an array
    return -1

## Driver code
arr = [20, 30, 40, 50, 60, 70, 80, 90]
x = 20
i = 0
j = len(arr) - 1
## function calling
result = binarySearch(arr, x, i, j)
print("Searching element is present at the location:",result)