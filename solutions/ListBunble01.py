import math
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
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss in d:
                d[ss].append(s)
            else:
                d[ss] = [s]
        return [x for x in d.values()]
        
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        L = len(arr)
        max1 = -1
        for i in range(L-1,-1,-1):
            ans.append(max1)
            max1 = max(max1, arr[i])
        return ans[::-1]
                
    def isSubsequence(self, s: str, t: str) -> bool:
        L = len(s)
        i = 0
        j = 0
        located = 0
        while j < len(t):
            if located == L: return True
            if s[i]==t[j]:
                i+=1;
                located+=1
            j+=1
        return True if located==L else False  
        
    def lengthOfLastWord(self, s: str) -> int:
        snew = s.rstrip();
        j = len(snew)-1
        while j>-1:
            if snew[j]==' ': break;
            j-=1
        return (len(snew)-1)-j
    
    def longestCommonPrefix_1(self, strs: List[str]) -> str:
        ans = "";
        sstrs = sorted(strs)
        left = sstrs[0]
        right = sstrs[-1]
        for i in range(min(len(left), len(right))):
            if left[i]!=right[i]:
                break
            ans+=left[i]
        return ans

    def longestCommonPrefix_2(self, strs: List[str]) -> str:
        if strs is None or len(strs)==0: return ""
        prefix = strs[0]
        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[0:len(prefix)-1]
        return prefix
    
    def topKFrequent_1(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n]=d.get(n,0)+1
        sd = dict(reversed(sorted(d.items(), key=lambda item: item[1])))
        return list(sd)[:k]
    
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            for c in s:
                i = ord(c) << 2
                ans += chr(i) 
            ans += chr(10) 
        return ans 

    def decode(self, s: str) -> List[str]:
        ans = []
        element = ""
        for c in s:
            if c == chr(10):
                ans.append(element)
                element = ""
            else:
                i = ord(c) >> 2
                element += chr(i)
        return ans

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        left = 1
        for i in range(len(nums)):
            ans[i] = left
            left = left * nums[i]

        right = 1
        for i in reversed(range(len(nums))):
            ans[i] = right * ans[i]
            right = right * nums[i]

        return ans