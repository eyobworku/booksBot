n = int(input())
lst = [int(x) for x in input().split()]
minIn = 0
maxIn = n-1
for x in range(n):
    if lst[x] <= lst[minIn]:
        minIn = x

    if lst[x] > lst[maxIn] or lst[x] == lst[maxIn] and x < maxIn:
        maxIn = x

if minIn == maxIn:
    res = 0
else:
    res = abs(0 - maxIn) + (n-1) - minIn
    if minIn < maxIn:
        res-=1

print(res)

# import math

# with open('input.txt', 'r') as f_input, open('output.txt', 'w') as f_output:
#     a,b = map(int, f_input.readline().split())
#     n = min(a,b)
#     m = abs(a-b)
#     x = math.ceil(m/2)
#     if a>b:
#         mid = 'GB'
#         fir = 'B'
#     else:
#         mid = 'BG'
#         fir = 'G'
#     res = ''
#     for _ in range(x):
#         res += fir
#     for _ in range(n):
#         res += mid
#     for _ in range(x,m):
#         res += fir
#     f_output.write(res)
# with open('input.txt', 'r') as f_input, open('output.txt', 'w') as f_output:
#     n, m = map(int, f_input.readline().split())
 
#     res = ""
 
#     if n > m:
#         res += 'B'
#         n -= 1
#     else:
#         res += 'G'
#         m -= 1
 
#     while n > 0 or m > 0:
#         if res[-1] == 'B':
#             res += 'G'
#             m -= 1
#         else:
#             res += 'B'
#             n -= 1
 
#     f_output.write(res)



# with open('input.txt', 'r') as f_input, open('output.txt', 'w') as f_output:
#     n, m = map(int, f_input.readline().split())

#     res = ""

#     if n > m:
#         res += 'B'
#         n -= 1
#     else:
#         res += 'G'
#         m -= 1

#     while n > 0 or m > 0:
#         if res[-1] == 'B':
#             res += 'G'
#             m -= 1
#         else:
#             res += 'B'
#             n -= 1

#     f_output.write(res)
