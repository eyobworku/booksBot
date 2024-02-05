from collections import Counter

def find_frequent(arr):
    counter = Counter(arr)
    max_count = max(counter.values())
    frequency = max_count
    return frequency

class NumberArray:
    def __init__(self, length, numbers):
        self.length = length
        self.numbers = numbers

    def get_length(self):
        return self.length

    def get_numbers(self):
        return self.numbers
    
prob_no = int(input())

data = []
for z in range(prob_no):
    leng = int(input())
    nums = [ int(x) for x in input().split()]
    data.append(NumberArray(leng,nums))

res = []
for x in data:
    hop = []
    for i in range(x.get_length()):
        j = x.get_numbers()[i]
        while j <= x.get_length():
            hop.append(j)
            j = j + x.get_numbers()[i]
    if len(hop) == 0:
        res.append(0)
    else:
        res.append(find_frequent(hop))

for x in res:
    print(x)


# with open('input.txt', 'r') as f_input:
#     prob_no = int(f_input.readline())

#     data = []

#     for z in range(prob_no):
#         leng = int(f_input.readline())
#         nums = [ int(x) for x in f_input.readline().split()]
#         data.append(NumberArray(leng,nums))

# for x in data:
#     print('leng: ', x.get_length())
#     print('nums: ', x.get_numbers())