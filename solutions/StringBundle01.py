import math
from typing import Counter, List


class StringBundle01:
    def is_isomorphic(self, s1:str, s2:str) -> bool:
        if len(s1) != len(s2):
            return False

        m1, m2 = {}, {}

        for i in range(len(s1)):
      
            # If character not seen before, store 
            # its first occurrence index
            if s1[i] not in m1:
                m1[s1[i]] = i
            if s2[i] not in m2:
                m2[s2[i]] = i

            # Check if the first occurrence indices match
            if m1[s1[i]] != m2[s2[i]]:
                return False
            
        return True

    def lengthOfLongestSubstring_1(self, s: str) -> int:
        longest = 0
        for i in range (len(s)):
            ss = [s[i]]
            j = i + 1
            while j < len(s):
                c = s[j]
                if c in ss:
                    break
                else:
                    ss.append(c)
                j+=1
            longest = max(len(ss), longest)
        return longest   
    
    def lengthOfLongestSubstring_2(self, s: str) -> int:
        ans = 0
        queue = []
        for i in range(len(s)):
            c = s[i]
            while c in queue:
                queue.pop(0)
            queue.append(c)
            ans = max(ans, len(queue))
        return ans
    
    def characterReplacement(self, s: str, k: int) -> int:
        counter={}
        left = 0
        ans = 0
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right],0) + 1 
            f = (right - left + 1) - max(counter.values()) 
            if f == k:
                ans = max(ans, right - left + 1)            
            elif f > k:
                counter[s[left]] -= 1
                left += 1
        return ans 

    def isValidParentheses(self, s: str) -> bool:
        pOpened = [ '(', '{', '[' ]
        pClosed = [ ')', '}', ']' ]
        stack = []
        for c in s:
            if c in pOpened:
                stack.append(c)
            if c in pClosed:
                index = pClosed.index(c)
                if len(stack)>0 and stack[len(stack)-1]==pOpened[index]:
                    stack.pop()
                else:
                    return False
        return True if len(stack)==0 else False
    
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []
        def backtracking(opened, closed) -> None:
            if opened == closed == n:
                ans.append("".join(stack))
            if closed < opened:
                stack.append(")")
                backtracking(opened, closed+1)
                stack.pop()
            if opened < n:
                stack.append("(")
                backtracking(opened+1, closed)
                stack.pop()
        backtracking(0,0)
        return ans

    def checkInclusion_1(self, s1: str, s2: str) -> bool:    
        if s1 in s2: return True
        perms = []
        def findPermutations(string, i = 0):
            if i == len(string):   	 
                perms.append("".join(string))
                return
            for j in range(i, len(string)):
                words = [c for c in string]
                words[i], words[j] = words[j], words[i]
                findPermutations(words, i + 1)
        findPermutations(s1)
        for p in perms:
            if p in s2: 
                return True 
        return False    
          
    def checkInclusion_2(self, s1: str, s2: str) -> bool:
        L = len(s1)
        L2 = len(s2)
        def frequencies (s: str) -> dict:
            freq = {}
            for c in s:
                f = freq.get(c,0)
                freq[c] = f + 1
            return freq
        fs1 = frequencies(s1)
        i = 0        
        while i <= (L2 - L):
            if s2[i] in s1:
                sfs2 = frequencies(s2[i:i+L])
                if sfs2 == fs1:  return True
            i+=1
        return False
    
    def checkInclusion_3(self, s1: str, s2: str) -> bool:
        L = len(s1)
        L2 = len(s2)
        cnt1 = Counter(s1)
        i = 0        
        while i <= (L2 - L):
            if s2[i] in s1:
                cnt2 = Counter(s2[i:i+L])
                if cnt1==cnt2: return True
            i+=1
        return False
    
    def minWindow(self, s: str, t: str) -> str:
        cnt = Counter(t)
        memo = {}
        for c in t: memo[c]=memo.get(c,0)
        Ls = len(s)
        Rlen, Rstart = float("infinity"), 0
        left, right = 0, 0
        have = 0
        should = sum(cnt.values())
        
        while right<Ls:
            while have < should:  # add element to window
                idx = memo.get(s[right], -1) 
                if idx >= 0: 
                    memo[s[right]] = memo[s[right]] + 1
                    if memo[s[right]] <= cnt[s[right]]: have = have + 1
                right = right + 1
                if right==Ls: break
            
            while have >= should: # shink element from window
                if len(s[left:right]) < Rlen:
                    Rlen = right - left
                    Rstart = left
                idx = memo.get(s[left], -1)
                if idx >= 0: 
                    memo[s[left]] = memo[s[left]] - 1
                    if memo[s[left]] < cnt[s[left]]: have = have - 1
                left = left + 1
                
        return "" if Rlen==float("infinity") else s[Rstart:Rstart+Rlen]

        
        


