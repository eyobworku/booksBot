from collections import deque

# Create a deque
my_deque = deque()

# Append elements to the right end of the deque
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)

# Append elements to the left end of the deque
my_deque.appendleft(0)

# Print the deque
print(my_deque)  # Output: deque([0, 1, 2, 3])

# Access elements in the deque
print(my_deque[0])  # Output: 0
print(my_deque[-1])  # Output: 3

# Remove elements from the right end of the deque
last_element = my_deque.pop()
print(last_element)  # Output: 3

# Remove elements from the left end of the deque
first_element = my_deque.popleft()
print(first_element)  # Output: 0

# Print the updated deque
print(my_deque)  # Output: deque([1, 2])