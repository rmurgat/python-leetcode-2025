import math
from typing import List
import numpy as np

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
    
    def generatePascalTriangle(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        last_row = [1]
        for i in range (1, numRows):
            row = [0]*(i+1)
            L = len(row)
            mid = math.floor(len(last_row)/2)
            last = 0
            for left in range (mid+1):
                row[left]=last+last_row[left]
                last = last_row[left]
            idx = 0
            for right in range (L-1, mid, -1):
                row[right] = row[idx]
                idx+=1
            if L % 2 != 0:
                row[mid] = last_row[mid]+last_row[mid]
            ans.append(row.copy())
            last_row = row.copy()
        return ans   
    
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        def getValidEmail(s: str) -> str:
            part = s.split("@")
            local = part[0].split("+")
            real = local[0].replace(".","")
            return real + "@" + part[1]

        for e in emails:
            correct = getValidEmail(e)
            ans.add(correct)

        return len(ans)
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:    
        counter = 0
        subcounter = 1
        for i in range (len(flowerbed)):
            if subcounter==3:
                counter = counter + 1
                subcounter = 1
            if flowerbed[i] == 0:
                subcounter = subcounter + 1
            else:
                subcounter = 0
        if subcounter>1:
            counter = counter + 1
        return True if counter >= n else False
    
    def majorityElement_1(self, nums: List[int]) -> int:
        memo = {}
        majority = math.ceil(len(nums)/2)
        for i in nums:
            located = memo.get(i,None)
            if located:
                memo[i]=located+1
                if located+1>=majority:
                    return i
            else:
                memo[i]=1
        return 0

    def majorityElement_2(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if count==0: res = n
            if res != n:
                count-=1
            else:
                count+=1
        return res
    
    def nextGreaterElement_1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n in nums1:
            greater = -1
            for i in range(len(nums2)-1,-1,-1):
                if nums2[i]>n:
                    greater = nums2[i]
                if nums2[i]==n:
                    ans.append(greater)
                    break
        return ans
    
    def nextGreaterElement_2(self, nums1: List[int], nums2: List[int]) -> List[int]:    
        memo = {n:i for i,n in enumerate(nums1)}
        ans = [-1]*len(nums1)
        for n in nums1:
            idx = nums2.index(n)
            for i in range(idx, len(nums2)):
                if nums2[i] > n:
                    index = memo[n]
                    ans[index]=nums2[i]
                    break
        return ans

    def nextGreaterElement_3(self, nums1: List[int], nums2: List[int]) -> List[int]:    
        memo = {n:i for i,n in enumerate(nums1)}
        ans = [-1]*len(nums1)
        for i in range(len(nums2)):
            if nums2[i] not in memo:
                continue
            for j in range (i+1, len(nums2)):
                if nums2[j]>nums2[i]:
                    idx = memo[nums2[i]]
                    ans[idx] = nums2[j]
                    break
        return ans
    
    def pivotIndex(self, nums: List[int]) -> int:
        L = len(nums)
        aleft,aright, left,right, sumleft, sumright = [0]*L, [0]*L, 0, L-1, 0, 0
        while left<L:
            aleft[left]=sumleft
            aright[right]=sumright
            sumleft+=nums[left]
            sumright+=nums[right]
            left+=1
            right-=1
        for left in range(0,L):
            if aleft[left]==aright[left]:
                return left
        return -1

        
    def sumRange(self, nums: List[int], left: int, right: int) -> int:
        prefixsum = [0]
        for num in nums:
            prefixsum.append(prefixsum[-1]+num)

        return prefixsum[right+1]-prefixsum[left]
