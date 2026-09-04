# 0/1 Knapsack using Top-Down Dynamic Programming

def knapsack(weights, values, n, capacity, memo):

    # Base condition
    if n == 0 or capacity == 0:
        return 0

    # Check if result is already calculated
    if memo[n][capacity] != -1:
        return memo[n][capacity]

    # If item is too heavy, don't include it
    if weights[n - 1] > capacity:
        memo[n][capacity] = knapsack(
            weights, values, n - 1, capacity, memo
        )

    else:
        # Include the item
        include = values[n - 1] + knapsack(
            weights, values, n - 1,
            capacity - weights[n - 1], memo
        )

        # Exclude the item
        exclude = knapsack(
            weights, values, n - 1, capacity, memo
        )

        # Store maximum value
        memo[n][capacity] = max(include, exclude)

    return memo[n][capacity]


# Input
weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]
capacity = 5

n = len(weights)

# Create memoization table
memo = [[-1] * (capacity + 1) for _ in range(n + 1)]

# Find maximum value
result = knapsack(weights, values, n, capacity, memo)

print("Maximum Value:", result)
