inp = []
for _ in range(3):
    inp.append([ int(x) for x in input().split()])

# with open('input.txt', 'r') as f_input:
#     for _ in range(3):
#         inp.append([ int(x) for x in f_input.readline().split()])

res = [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]

def update(i,j):
    res[i][j] ^= 1

    if i > 0:
        res[i - 1][j] ^= 1
    if i < 2:
        res[i + 1][j] ^= 1
    if j > 0:
        res[i][j - 1] ^= 1
    if j < 2:
        res[i][j + 1] ^= 1
        

for i in range(3):
    for j in range(3):
        if inp[i][j] % 2 != 0:
            update(i,j)

for x in res:
    print(''.join(str(y) for y in x))