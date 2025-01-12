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

    def productExceptSelf_1(self, nums: List[int]) -> List[int]:
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
    
    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        forw, backw = [0]*len(nums), [0]*len(nums)
        last = 1
        for i in range(len(nums)):
            forw[i] = last
            last = nums[i]*last
        last = 1
        for i in range(len(nums)-1,-1,-1):
            backw[i] = last
            last = nums[i]*last
            ans[i] = backw[i] * forw[i]

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


    def findDisappearedNumbers_1(self, nums: List[int]) -> List[int]:
        L = len(nums)
        dm = { i:0 for i in range(1,L+1) }
        for n in nums:
            dm[n] = dm[n] + 1
        return [n for n,cnt in dm.items() if cnt==0]
    
    def findDisappearedNumbers_2(self, nums: List[int]) -> List[int]:
        L = len(nums)
        lm = [False]*(L)
        for n in nums:
            lm[n-1]=True
        return [i+1 for i,b in enumerate(lm) if not b]

    def maxNumberOfBalloons_1(self, text: str) -> int:
        lmemo = []
        for ch in text:
            if ch not in "balloon": continue
            located = False
            for lm in lmemo:
                if len(lm)==0: continue
                if ch in lm:
                    lm.remove(ch)
                    located = True
                    break
            if not located:
               nb = [c for c in "balloon"]
               nb.remove(ch)
               lmemo.append(nb) 
        ans = 0
        for lm in lmemo:
            if len(lm)==0: 
                ans+=1
        return ans           

    def maxNumberOfBalloons_2(self, text: str) -> int:
        lmemo = []
        for ch in text:
            if ch not in "balloon": continue
            located = False
            for i in range (len(lmemo)):
                if len(lmemo[i])==0: continue
                if lmemo[i].find(ch)!=-1:
                    lmemo[i] = lmemo[i].replace(ch,"",1)
                    located = True
                    break
            if not located:
               nb = "balloon"
               nb = nb.replace(ch,"",1)
               lmemo.append(nb[:]) 
        ans = 0
        for lm in lmemo:
            if lm=="": 
                ans+=1
        return ans      
    
    def wordPattern(self, pattern: str, s: str) -> bool:
        dpattern = {}
        dword = {}
        counter = 0
        for c in pattern:
            if c not in dpattern:
                dpattern[c]=counter
                counter += 1

        counter = 0
        lwords = s.split()
        for word in lwords:
            if word not in dword:
                dword[word]=counter
                counter += 1

        if len(pattern)!=len(lwords): return False

        for i in range (len(pattern)):
            ch = pattern[i]
            word = lwords[i]
            pos1 = dpattern[ch]
            pos2 = dword[word]
            if pos1!=pos2: return False

        return True   
    
    def twoSumII_1(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            fix = numbers[i]
            left = i + 1
            right = len(numbers)-1
            while left < right:
                mid = math.floor( (right - left)/2 )
                sum = fix + numbers[mid]
                if sum == target: 
                    return [ fix, numbers[mid] ]
                if sum < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return []
    
    def twoSumII_2(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            csum = numbers[left] + numbers[right]
            if csum == target: 
                return [ left+1, right+1 ]
            if csum < target:
                left += 1
            else:
                right -= 1
        return []    
    
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        s, maxs, last = 0,0,nums[0]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==last:
                continue

            if last+1 == nums[i]:
                s += 1
            else:
                maxs = max(maxs, s)
                s = 1
            last = nums[i]
        return max(maxs, s)
    
    def trap(self, height: List[int]) -> int:
        maxRight = [0]*len(height)
        ans = 0
        maxh = 0
        for i in range(len(height)-1,-1,-1):
            maxRight[i] = maxh
            maxh = max(maxh, height[i])
        maxh = 0
        for i in range(len(height)):
            vol = min(maxh,maxRight[i]) - height[i]
            if vol>0:
                ans+=vol
            maxh = max(maxh, height[i])
        return ans
    
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minbuy = prices[0]
        for i in range (len(prices)):
            if prices[i]<minbuy:
                minbuy = prices[i]
            profit = prices[i] - minbuy
            ans = max(ans,profit)
        return ans 
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]* len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            n  = temperatures[i]
            while stack and stack[-1][0]<=n:
                stack.pop()
            if stack and stack[-1][0]>n:
                ans[i] = stack[-1][1]-i
            stack.append([n,i])
        return ans  

    def binarySearch(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = math.floor( (r - l) / 2 ) + l
            print("mid",mid)
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                return mid
        return -1
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            match t:
                case "+":
                    res = (int(stack.pop()) + int(stack.pop()))
                    stack.append(res)
                case "-":
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())         
                    res = num2 - num1
                    stack.append(res)
                case "*":
                    res = (int(stack.pop()) * int(stack.pop()))
                    stack.append(res)
                case "/":
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())         
                    res = num2 / num1
                    stack.append(res)
                case _:
                    stack.append(t)
        return int(res)

    def monotonicStackIncreasing(self, nums):
        stack = []
        ans = []
        for n in nums:
            #if len(stack) > 0: print ("stack:", stack)
            while stack and stack[-1] > n:
                stack.pop()
            stack.append(n)
        while stack:
            ans.insert(0, stack.pop())
        return ans

    def monotonicStackDecreasing(self, nums):
        stack = []
        ans = []
        for n in nums:
            #if len(stack) > 0: print ("stack:", stack)
            while stack and stack[-1] < n:
                stack.pop()
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(-1)                
            
            stack.append(n)
        return ans
