from collections import defaultdict

def calculate_max_frequency(arr):
    mults = defaultdict(int)
    for num in arr:
        mults[num] += 1

    tot = [0] * (len(arr) + 1)
    ans = 0
    for i in range(1, len(arr) + 1):
        curr_mult = i
        while curr_mult <= len(arr):
            tot[curr_mult] += mults[i]
            curr_mult += i

        ans = max(ans, tot[i])

    return ans

prob_no = int(input())
for _ in range(prob_no):
    n = int(input())
    array = list(map(int, input().split()))
    result = calculate_max_frequency(array)
    print(result)
