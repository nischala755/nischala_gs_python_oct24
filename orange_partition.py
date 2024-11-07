def partition_oranges():
    # Read the number of oranges
    n = int(input())
    # Read the diameters of the oranges
    oranges = list(map(int, input().split()))
    
    # The last orange is the pivot
    pivot = oranges[-1]
    k = 0  # Pointer for the position to swap

    # Partitioning process
    for i in range(n - 1):
        if oranges[i] <= pivot:
            # Swap oranges[i] with oranges[k]
            oranges[i], oranges[k] = oranges[k], oranges[i]
            k += 1

    # Place the pivot in its correct position
    oranges[k], oranges[-1] = oranges[-1], oranges[k]

    # Print the resultant array
    print(" ".join(map(str, oranges)))

# Call the function
partition_oranges()