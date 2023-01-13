def spiral_print(matrix, m, n):
    k = 0 # starting row index
    l = 0 # starting column index

    while (k < m and l < n):
        for i in range(l, n):
            print(matrix[k][i], end=" ")
        k += 1
        for i in range(k, m):
            print(matrix[i][n-1], end=" ")
        n -= 1
        if (k < m):
            for i in range(n-1, (l-1), -1):
                print(matrix[m-1][i], end=" ")
            m -= 1
        if (l < n):
            for i in range(m-1, k-1, -1):
                print(matrix[i][l], end=" ")
            l += 1

# Test
rows = int(input())
cols = int(input())
matrix = []
for i in range(rows):
    matrix.append(list(map(int, input().split())))
spiral_print(matrix, rows, cols)
