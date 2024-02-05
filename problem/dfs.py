def dfs(graph, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)  # Process the current node

            # Add unvisited neighbors to the stack
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Start DFS from node 'A'
dfs(graph, 'A')