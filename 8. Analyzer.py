import numpy as np

def create_array():
    print("\nArray Creation:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of elements: "))
        data = list(map(int, input("Enter elements: ").split()))
        return np.array(data[:n])

    elif choice == 2:
        r = int(input("Enter the number of rows: "))
        c = int(input("Enter the number of columns: "))
        data = list(map(int, input(f"Enter {r*c} elements separated by space: ").split()))
        return np.array(data).reshape(r, c)

    elif choice == 3:
        x = int(input("Enter first dimension: "))
        y = int(input("Enter second dimension: "))
        z = int(input("Enter third dimension: "))
        data = list(map(int, input(f"Enter {x*y*z} elements: ").split()))
        return np.array(data).reshape(x, y, z)

def math_operations(arr):
    print("\nMathematical Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice: "))

    data = list(map(int, input(f"Enter the same-size array elements ({arr.size} elements separated by space): ").split()))
    arr2 = np.array(data).reshape(arr.shape)

    if choice == 1:
        print("\nResult of Addition:\n", arr + arr2)
    elif choice == 2:
        print("\nResult of Subtraction:\n", arr - arr2)
    elif choice == 3:
        print("\nResult of Multiplication:\n", arr * arr2)
    elif choice == 4:
        print("\nResult of Division:\n", arr / arr2)

def combine_split(arr):
    print("\nCombine or Split Arrays:")
    print("1. Combine Arrays")
    print("2. Split Array")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = list(map(int, input(f"Enter elements of another array ({arr.size} elements separated by space): ").split()))
        arr2 = np.array(data).reshape(arr.shape)
        combined = np.vstack((arr, arr2))
        print("\nCombined Array (Vertical Stack):\n", combined)

    elif choice == 2:
        splits = int(input("Enter number of splits: "))
        result = np.array_split(arr, splits)
        print("\nSplit Arrays:")
        for r in result:
            print(r)

def search_sort_filter(arr):
    print("\nSearch, Sort, and Filter:")
    print("1. Search a value")
    print("2. Sort the array")
    print("3. Filter values")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value to search: "))
        print("Found at positions:", np.where(arr == val))

    elif choice == 2:
        print("\nSorted Array:")
        print(np.sort(arr, axis=1))
        print("(Sorting applied row-wise.)")

    elif choice == 3:
        val = int(input("Show values greater than: "))
        print(arr[arr > val])

def statistics(arr):
    print("\nAggregates and Statistics:")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Standard Deviation")
    print("5. Variance")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Sum:", np.sum(arr))
    elif choice == 2:
        print("Mean:", np.mean(arr))
    elif choice == 3:
        print("Median:", np.median(arr))
    elif choice == 4:
        print("Standard Deviation:", np.std(arr))
    elif choice == 5:
        print("Variance:", np.var(arr))

def main():
    arr = None
    while True:
        print("\nWelcome to the NumPy Analyzer!")
        print("1. Create a NumPy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            arr = create_array()
            print("\nArray created successfully:\n", arr)

        elif choice == 2 and arr is not None:
            math_operations(arr)

        elif choice == 3 and arr is not None:
            combine_split(arr)

        elif choice == 4 and arr is not None:
            search_sort_filter(arr)

        elif choice == 5 and arr is not None:
            statistics(arr)

        elif choice == 6:
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break

        else:
            print("Please create an array first.")


a = main()