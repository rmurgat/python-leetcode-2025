import math
from typing import List


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
