def getMinimumCost(c, k):
    # Sort the flower prices in descending order
    c.sort(reverse=True)
    
    total_cost = 0
    # Iterate over each flower
    for i in range(len(c)):
        # Calculate cost: (i // k + 1) * price of the flower
        total_cost += (i // k + 1) * c[i]
    
    return total_cost

# Example Usage
if __name__ == "__main__":
    # Sample Input
    n, k = 3, 3
    c = [2, 5, 6]
    print(getMinimumCost(c, k))  # Output: 13
