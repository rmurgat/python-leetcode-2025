from typing import List


class ListBundle01:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        nums.sort()
        L = len(nums)
        for i in range(L):

            located = memo.get(target - nums[i], None)
            if located is not None:
                return [ i, located ]
            
            memo[nums[i]] = i

        return [] 
    
    def hasDuplicate_1(self, nums: List[int]) -> bool:
        s = set(nums)
        return True if len(s)!=len(nums) else False
    
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            located = d.get(c,None)
            if not located is None:
                d[c] = located+1
            else:
                d[c] = 1
        for c in t:
            located = d.get(c,None)
            if not located is None:
                d[c] = d[c]-1
            else:
                return False
        dif = [x for x,y in d.items() if y!=0]
        return True if len(dif)==0 else False
                

        