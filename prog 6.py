import timeit
import random
import matplotlib.pyplot as plt

# Input Array elements
def Input(Array, n):
    # iterating till the range
    for i in range(0, n):
        ele = random.randrange(1, 50)  # adding the element
        Array.append(ele)

# divide function
def partition(Array, low, high):
    i = low - 1
    pivot = Array[high]  # pivot element

    for j in range(low, high):
        if Array[j] <= pivot:
            i += 1
            Array[i], Array[j] = Array[j], Array[i]

    Array[i + 1], Array[high] = Array[high], Array[i + 1]
    return i + 1

# Quick sort
def quickSort(Array, low, high):
    if low < high:
        pi = partition(Array, low, high)
        quickSort(Array, low, pi - 1)
        quickSort(Array, pi + 1, high)

# Main Block
N = []
CPU = []
trail = int(input("Enter no. of trials: "))
for t in range(trail):
    Array = []
    print("> TRIAL NO:", t + 1)
    n = int(input("Enter number of elements: "))
    Input(Array, n)
    start = timeit.default_timer()
    quickSort(Array, 0, n - 1)
    end = timeit.default_timer()
    print("Sorted Array:")
    print(Array)
    N.append(n)
    CPU.append(round((end - start) * 1000000, 2))

print("N\tCPU")
for t in range(trail):
    print(N[t], "\t", CPU[t])

# Plotting Graph
plt.plot(N, CPU)
plt.scatter(N, CPU, color="red", marker="o", s=50)
plt.xlabel('Array Size N')
plt.ylabel('CPU Processing Time')
plt.title('Quick Sort Time Efficiency')
plt.show()
