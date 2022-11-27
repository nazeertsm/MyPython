## Implementation of Insertion Sort
## Time Complexity: O(n^2)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


## Driver code
#arr = [75, 90, 100, 95, 85, 80]
arr = [75, 90, 100, 195, 85, 10]
result = insertion_sort(arr)
print("Sorted array after applying the insertion sort:", result)