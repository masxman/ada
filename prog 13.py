import sys

def minKey(key, mstSet, n):
    min_value = sys.maxsize
    for v in range(n):
        if not mstSet[v] and key[v] < min_value:
            min_value = key[v]
            min_index = v
    return min_index

def printMST(parent, c, n):
    totalWeight = 0
    print("Edge Weight")
    for i in range(1, n):
        print(f"{parent[i]+1} - {i+1} {c[i][parent[i]]}")
        totalWeight += c[i][parent[i]]
    return totalWeight

def primMST(c, n):
    parent = [None] * n
    key = [sys.maxsize] * n
    mstSet = [False] * n
    key[0] = 0
    parent[0] = -1

    for count in range(n):
        u = minKey(key, mstSet, n)
        mstSet[u] = True
        for v in range(n):
            if c[u][v] > 0 and not mstSet[v] and c[u][v] < key[v]:
                parent[v] = u
                key[v] = c[u][v]

    totalWeight = printMST(parent, c, n)
    print(f"Total cost of the minimum spanning tree: {totalWeight}")

# Main Code
n = int(input("Enter the number of vertices: "))
C = []
print("Enter the cost adjacency matrix:")
for i in range(n):
    C.append(list(map(int, input().split())))

primMST(C, n)
