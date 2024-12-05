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

        