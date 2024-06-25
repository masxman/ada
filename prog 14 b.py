def warshalls(c, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if c[i][j] or (c[i][k] and c[k][j]):
                    c[i][j] = 1

    print("The transitive closure of the graph is:")
    for i in range(n):
        for j in range(n):
            print(c[i][j], end=" ")
        print()

def main():
    n = int(input("Enter the number of vertices: "))
    C = []
    print("Enter the adjacency cost matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        C.append(row)

    warshalls(C, n)

main()
