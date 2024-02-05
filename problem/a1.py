
testCase = int(input())
 
for _ in range(testCase):
    n = int(input())
    v = list(map(int, input().split()))
    total_sum = sum(v)
    temp, mini, count = 0, n, 0
 
    for i in range(n):
        temp += v[i]
        count += 1
        temp_maxo = 0
 
        if total_sum % temp == 0:
            temp_maxo = count
            temp_sum, temp_count = 0, 0
 
            for j in range(i + 1, n):
                temp_sum += v[j]
                temp_count += 1
 
                if temp_sum == temp:
                    temp_maxo = max(temp_maxo, temp_count)
                    temp_sum = 0
                    temp_count = 0
 
            if temp_sum == 0:
                mini = min(mini, temp_maxo)
 
    print(mini)