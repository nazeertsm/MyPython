#function definition
#time complexity : o(n)
#space complexity:  0(1)

def linearSearch(arr, x):

    for i in range(len(arr)):
        if arr[i]==x:
            return i
            
    return -1

#Driver code
arr = [2, 4, 7, 1, 9]
x=7
#function calling
result  = linearSearch(arr, x)
print("searching element is present at index", result)
