N, L = map(int, input().split())
points = tuple(tuple(map(int, input().split())) for _ in range(L))
counts = [0] * L

i = 0
while i < N:
    max_index = 0
    max_point = 0
    for k in range(L):
        if (points[k][i] > max_point):
            max_point = points[k][i]
            max_index = k
    counts[max_index] += 1
    i += 1

k = 0
max_index = 0
max_count = 0
while k < L:
    if counts[k] > max_count:
        max_index = k
        max_count = counts[k]
    k += 1

print(f'{max_index + 1} {max_count}')
