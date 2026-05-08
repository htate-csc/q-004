n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*map(lambda x, y: x - y, A, B))

# i = 0
# while i < n:
#     print(A[i] - B[i], end='')
#     if i < n - 1:
#         print(' ', end='')
#     i += 1
