def max_sub(A):
    max_ending = temp_max = A[0]
    for i in A[1:]:
        max_ending = max(i, max_ending + i)
        temp_max = max(temp_max, max_ending)
    return temp_max

p = int(input().split()[1])
print(max_sub(list(map(lambda z: int(z) - p, input().split()))))
