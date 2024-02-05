prob_no = int(input())
for _ in range(prob_no):
    length = int(input())
    dic = {0:0}
    for x in input().split():
        j=x= int(x)
        while x <= length:
            dic[x] = dic.get(x, 0) + 1
            x+=j
    print(max(dic.values()))


# prob_no = int(input())
# res = []

# for z in range(prob_no):
#     length = int(input())
#     count_dict = {}
#     for x in map(int, input().split()):
#         j = x
#         while x <= length:
#             count_dict[x] = count_dict.get(x, 0) + 1
#             x += j
#     res.append(max(count_dict.values()))

# for count in res:
#     print(count)



# with open('input.txt', 'r') as f_input:
#     prob_no = int(f_input.readline())

#     data = []
#     res = []

#     for z in range(prob_no):
#         length = int(f_input.readline())
#         array = [0] * (length+1)
#         for x in f_input.readline().split():
#             x = int(x)
#             j =x
#             while x <= length:
#                 array[x]+=1
#                 x+=j
#         res.append(max(array))
 
# for x in res:
#     print(x)



 
# prob_no = int(input())
 


# for z in range(prob_no):
#     length = int(input())
#     numbers = [int(x) for x in input().split()]
