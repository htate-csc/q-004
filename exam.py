n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*map(lambda x, y: x - y, A, B))

# # 別解
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# answer = []
# for i in range(N):
#     answer.append(A[i] - B[i])
# print(' '.join(map(str, answer)))

# i = 0
# while i < n:
#     print(A[i] - B[i], end='')
#     if i < n - 1:
#         print(' ', end='')
#     i += 1
