from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = len(height)
        maxim = 0
        for j in range(i):
            for x in range(j+1,i):
                y = x-j
                mini = min(height[j],height[x])
                z = y * mini
                if z > maxim:
                    maxim = z

        return maxim




solu = Solution()
height = [1,1]
print(solu.maxArea(height))