# from collections import Counter

# N = int(input())
# bar_lengths = list(map(int, input().split()))

# unique_lengths = set(bar_lengths)
# length_counts = Counter(bar_lengths)

# max_height = max(length_counts.values())

# num_towers = sum(count == max_height for count in length_counts.values())

# print(max_height, num_towers)

input()
lengths = list(map(int, input().split()))

bar_counts = {}
for length in lengths:
    if length not in bar_counts:
        bar_counts[length] = 1
    else:
        bar_counts[length] += 1

max_height = max(bar_counts.values())
total_towers = len(bar_counts)

print(max_height, total_towers)


