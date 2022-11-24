## Implementation of Bubble Sort
## Time complexity: O(n^2)
## Method implementation
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                ## swap of the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

## Driver code
arr = [70, 20, 50, 60, 35, 47]
result = bubbleSort(arr)
print("Array after using bubble sort is:", result)