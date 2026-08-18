import timeit


# 1. Recursive method
def fibonacci_recursive(num):
    if num <= 1:
        return num
    return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)


# 2. Memoization method
def fibonacci_memo(num, cache=None):
    if cache is None:
        cache = {}

    if num <= 1:
        return num

    if num in cache:
        return cache[num]

    cache[num] = fibonacci_memo(num - 1, cache) + fibonacci_memo(num - 2, cache)
    return cache[num]


# 3. Iterative DP method
def fibonacci_dp(num):
    if num <= 1:
        return num

    first, second = 0, 1

    for _ in range(2, num + 1):
        first, second = second, first + second

    return second


# 4. Fast doubling method
def fibonacci_fast(num):
    def get_pair(value):
        if value == 0:
            return 0, 1

        first, second = get_pair(value // 2)

        even = first * (2 * second - first)
        odd = first * first + second * second

        if value % 2 == 0:
            return even, odd
        return odd, even + odd

    return get_pair(num)[0]


if __name__ == "__main__":

    n = 12

    print(f"Fibonacci({n}) using different methods:\n")
    print(f"[1] Recursive method : {fibonacci_recursive(n)}")
    print(f"[2] Memoization      : {fibonacci_memo(n)}")
    print(f"[3] Iterative DP     : {fibonacci_dp(n)}")
    print(f"[4] Fast doubling    : {fibonacci_fast(n)}")

    print("\nFirst 12 Fibonacci numbers:")
    print([fibonacci_dp(i) for i in range(12)])

    n_test = 25

    recursive_time = timeit.timeit(
        lambda: fibonacci_recursive(n_test), number=1
    )

    dp_time = timeit.timeit(
        lambda: fibonacci_dp(n_test), number=1
    )

    print(f"\nTime taken for Fibonacci({n_test}):")
    print(f"Recursive method : {recursive_time:.5f} seconds")
    print(f"Iterative DP     : {dp_time:.8f} seconds")

    n_large = 80

    print(f"\nFibonacci({n_large}) using DP      : {fibonacci_dp(n_large)}")
    print(f"Fibonacci({n_large}) using doubling: {fibonacci_fast(n_large)}")
