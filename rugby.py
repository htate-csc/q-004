N, Q = map(int, input().split())
events = [tuple(map(int, input().split())) for _ in range(Q)]

counts = [0] * N

res = []

for e in events:
    match e[0]:
        case 1:
            counts[e[1] - 1] += 1
        case 2:
            counts[e[1] - 1] += 2
        case 3:
            if (counts[e[1] - 1] >= 2):
                res.append('Yes')
            else:
                res.append('No')
for r in res:
    print(r)
