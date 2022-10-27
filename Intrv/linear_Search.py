#Linear search is a method of finding elements within a list. It is also called a sequential search.  It is the simplest searching algorithm because it searches the desired element in a sequential manner.
#It compares each and every element with the value that we are searching for. If both are matched, the element is found, and the algorithm returns the key's index position.
def linear_Search(list1, n, key):  
  
    # Searching list1 sequentially  
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
  
  
list1 = [1 ,3, 5, 4, 7, 9]  
key = 7  
  
n = len(list1)  
res = linear_Search(list1, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)  