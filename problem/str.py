from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        if len(s)>len(t):
            return False
        j=0
        i=0
        while(i<len(t) and j<len(s)):
            if (s[j] == t[i]):
                i+=1
                j+=1
            else:
                i+=1

        if (j== len(s)):
            return True
        else:
            return False
    def maxOperations(self, nums: List[int], k: int) -> int:
        i = 0
        j = len(nums) -1
        res = 0
        while i < j:
            if nums[i] + nums[j] == k:
                i+=1
                j-=1
                res+=1
            elif nums[i] >= k:
                i+=1
            elif nums[j] >= k:
                j-=1
        return res
sol = Solution()
arr =[1,2,3,4]
47
res = sol.maxOperations(arr, 5)
print(res)