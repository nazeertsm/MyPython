## Time complexity: O(n)
## Two pointer approach
def two_sum(arr, target_sum):
    left = 0
    right = len(arr) - 1
    while left < right:
        if (arr[left] + arr[right] == target_sum):
            return left, right
        elif (arr[left] + arr[right] < target_sum):
            left += 1
        else:
            right -= 1
    return -1,-1
        
## Driver code
arr = [20, 40, 60, 80, 90, 120, 240]
target_sum = 210
result = two_sum(arr, target_sum)
print(result)