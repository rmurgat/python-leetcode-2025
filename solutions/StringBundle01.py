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
