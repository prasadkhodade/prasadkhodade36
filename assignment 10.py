import numpy as np


# Create array using a list
def create_array_from_list():
    return np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# Create array using arange
def create_array_with_arange():
    return np.arange(1, 11)


# Display array details
def describe_array(arr):
    print("Array :", arr)
    print("Data type (dtype):", arr.dtype)
    print("Shape :", arr.shape)
    print("Number of dims :", arr.ndim)
    print("Size (elements) :", arr.size)


if __name__ == "__main__":

    # Method 1
    arr1 = create_array_from_list()
    print("Array created with np.array([1, 2, ..., 10]):")
    describe_array(arr1)

    # Method 2
    print()
    arr2 = create_array_with_arange()
    print("Array created with np.arange(1, 11):")
    describe_array(arr2)

    # Check whether both arrays are same
    print()
    print("Are both arrays equal?", np.array_equal(arr1, arr2))

    # Vectorized operations
    print()
    print("Vectorized operations")
    print("arr1 * 2 :", arr1 * 2)
    print("arr1 + 100 :", arr1 + 100)
    print("sum(arr1) :", arr1.sum())
    print("mean(arr1) :", arr1.mean())

    # Indexing and slicing
    print()
    print("Indexing and slicing")
    print("First element :", arr1[0])
    print("Last element :", arr1[-1])
    print("First 5 values :", arr1[:5])
    print("Every other :", arr1[::2])