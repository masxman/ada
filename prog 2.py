def binary_search(data_list, key):
    """
    Perform binary search of key in data_list.
    Returns index if key is found and -1 otherwise.
    """
    lo = 0
    hi = len(data_list) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data_list[mid] < key:
            lo = mid + 1
        elif data_list[mid] > key:
            hi = mid - 1
        else:
            return mid  # Key found; return its index.
    return -1  # Key not found; return -1

# Test function
if __name__ == "__main__":
    print("Enter the number of runs: ")
    n_runs = int(input())

    for _ in range(n_runs):
        print("Enter size: ")
        size = int(input())

    data_list = [random.randint(0, size - 1) for _ in range(size)]
    data_list.sort()
    print("List generated.")

    start_time = time.time()
    index_found = binary_search(data_list, key)
    time_taken = time.time() - start_time

    if index_found != -1:
        print(f"Key {key} found at position {index_found}")
    else:
        print(f"Key {key} not found.")

    times.append(time_taken)
    # Plotting
    plt.figure(figsize=(10, 4))
    plt.plot(x_values, y_values, 'o-')
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Time Taken (milliseconds)')
    plt.grid(True)
    plt.title('Time Complexity')
if __name__ == '__main__':
    main()
