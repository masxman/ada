import time
import matplotlib.pyplot as plt

# Function to perform linear search
def linear_search(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i  # If key is found, return the index
    return -1  # If key is not found, return -1

# Function to run linear search multiple times and record results
def linear_search_multiple(r):
    results = []
    for _ in range(r):
        n = int(input("Enter the number of elements: "))
        arr = list(map(int, input("\nEnter the elements of an array: ").split()))
        key = int(input("\nEnter the key element to be searched: "))
        
        # Repeat the search operation multiple times to amplify the time taken
        repeat = 10000
        result = -1
        start = time.time()
        for _ in range(repeat):
            result = linear_search(arr, n, key)
        end = time.time()
        
        if result != -1:
            print(f"Key {key} found at position {result}")
        else:
            print(f"Key {key} not found")
        
        time_taken = (end - start) * 1000  # In milliseconds
        print(f"Time taken to search a key element = {time_taken:.2f} milliseconds\n")
        
        # Record number of elements and time taken
        results.append((n, time_taken))
    
    return results

# Function to plot results
def plot_results(results):
    # Extract data
    n_values = [result[0] for result in results]
    times = [result[1] for result in results]

    # Create plot
    plt.figure()
    plt.plot(n_values, times, '-')
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Time Taken (milliseconds)')
    plt.title('Linear Search Time Complexity')
    plt.grid(True)
    plt.show()

# Main function
r = int(input("Enter the number of runs: "))
results = linear_search_multiple(r)
plot_results(results)
