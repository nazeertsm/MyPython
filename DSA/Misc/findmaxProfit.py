## function definition
## time complexity: O(n)

def findmaxProfit(price):
    ## intialization
    minPrice = float('inf')
    maxProfit = 0
    
    for i in range(len(price)):
        if price[i] < minPrice:
            minPrice = price[i]
        elif price[i] - minPrice > maxProfit:
            maxProfit = price[i] - minPrice
    return maxProfit


## Driver code
price = [7,4,5,3,6,16]
maxProfit_value = findmaxProfit(price)
print("The maximum profit of buying and selling the stocks is:", maxProfit_value)