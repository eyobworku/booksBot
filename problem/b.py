import itertools


leng = int(input())
cost = [int(x) for x in input().split()]
sort_cost = sorted(cost)
qus_size = int(input())

prefix_sum = [0] + list(itertools.accumulate(cost))
sort_prefix_sum = [0] + list(itertools.accumulate(sort_cost))

for i in range(qus_size):
    n,a,b = map(int, input().split())
    array_sum = 0
    if n == 1:
        array_sum = prefix_sum[b] - prefix_sum[a-1]
    else:
        array_sum = sort_prefix_sum[b] - sort_prefix_sum[a-1]
    print(array_sum)

