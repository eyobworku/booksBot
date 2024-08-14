from collections import defaultdict,deque
# from heapq import heapify,heappop,heappush
# from typing import List
import sys
input = lambda:sys.stdin.readline().rstrip()
RI = lambda: int(input())
RII = lambda: map(int, input().split())
RILIST = lambda: list(RII())
class UnionFindSize:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1] * n
    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1
                
def find_cycle(n, adj):
  seen = [False] * n
  seen_from = [-1] * n
  seen[0] = True
  q = deque([0])
  while q:
    v = q.pop()
    for u in adj[v]:
      if u != seen_from[v]:
        if seen[u]:
          cycle = [False] * n
          cycle[u] = True
          cycle[seen_from[u]] = True
          cycle[v] = True
          while not cycle[seen_from[v]]:#build the cycle from here
            v = seen_from[v]
            cycle[v] = True
          return cycle
        else:
          seen[u] = True
          seen_from[u] = v
          q.append(u)
  return None
def calc_dist(n, adj, start):
  dist = [float("inf")] * n
  prev = [-1] * n
  dist[start] = 0
  queue = []
  heapq.heappush(queue, (0, start))
  while queue:
    d, v = heapq.heappop(queue)
    if d == dist[v]:
      for u in adj[v]:
        if d + 1 < dist[u]:
          dist[u] = d + 1
          prev[u] = v
          heapq.heappush(queue, (d + 1, u))
  return dist