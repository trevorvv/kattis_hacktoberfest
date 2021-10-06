def solve(row, i):
    global n, forbidden
    if i == n+1:
        return 1

    total = 0
    row[i] = 0
    total += solve(row, i+1)

    for j in range(1, i):
        if row[j] == 1 and i in forbidden[j]:
            return total
    row[i] = 1
    total += solve(row, i+1)
    return total

data = input().split()
n = int(data[0])
m = int(data[1])
forbidden, allowed = {}, set()

for i in range(1, n+1):
    forbidden[i] = set()

for i in range(m):
    data2 = input().split()
    f1 = int(data2[0])
    f2 = int(data2[1])
    forbidden[f1].add(f2)
    forbidden[f2].add(f1)

row = [0 for j in range(n+1)]
print(solve(row, 1))