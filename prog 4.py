import timeit
import random
import matplotlib.pyplot as plt

# Input Array elements
def Input(Array, n):
    # iterating till the range
    for i in range(0, n):
        ele = random.randrange(1, 50)
        # adding the element to the array

# Selection Sort
def selectionSort(Array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if Array[j] < Array[min_index]:
                min_index = j
        # swapping the elements to sort the array
        Array[ind], Array[min_index] = Array[min_index], Array[ind]

# Main Block
N = []
CPU = []
trail = int(input("Enter no. of trials: "))
for t in range(trail):
    Array = []
    print("--> TRIAL NO:", t + 1)
    n = int(input("Enter number of elements: "))
    Input(Array, n)
    start = timeit.default_timer()
    selectionSort(Array, n)
    times = timeit.default_timer() - start
    print("Sorted Array: ")
    print(Array)
    N.append(n)
    CPU.append(round(float(times) * 1000000, 2))

# Plotting Graph
plt.plot(N, CPU)
plt.scatter(N, CPU, color="red", marker="*", s=50)
# naming the x axis
plt.xlabel('Array Size - N')
# naming the y axis
plt.ylabel('CPU Processing Time')
# giving a title to the graph
plt.title("Selection Sort Time Efficiency")
# function to show the plot
plt.show()
