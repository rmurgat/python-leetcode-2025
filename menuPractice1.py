from solutions.ListBunble01 import *
from solutions.StringBundle01 import *
from solutions.MyHashSet import *
from solutions.MyHashMap import *
from solutions.MinStack import *
from solutions.MatrixBundle01 import *

def printingSumTwo():
    lib = ListBundle01()
    print ("Sum Two: ", lib.twoSum([2,7,11,15],9))

def printingContainsDuplicate():
    lib = ListBundle01()
    print ("[Contain Duplicates] ")
    print ("Answer #1: ", lib.hasDuplicate_1([1,2,3,1]))
    print ("Answer #2: ", lib.hasDuplicate_1([1,2,3,4]))

def printingValidAnagram():
    lib = ListBundle01()
    print ("[Valid Anagram] ")
    print ("Answer #1: ", lib.isAnagram("anagram", "nagaram"))

def printingGroupAnagram():
    lib = ListBundle01()
    print ("[Group Anagram]")
    print ("Answer No. 1", lib.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

def printingReplaceElements():
    lib = ListBundle01()
    print ("[Replace Element]")
    print ("Answer No. 1", lib.replaceElements([17,18,5,4,6,1]))

def printingIsSequence():
    lib = ListBundle01()
    print ("[Is Sequence]")
    print ("Answer No. 1: ", lib.isSubsequence("abc","ahbgdc"))

def printingLengthLastWord():
    lib = ListBundle01()
    print ("[Is Sequence]")
    print ("Answer No. 1: ", lib.lengthOfLastWord("   fly me   to   the moon  "))
    print ("Answer No. 2: ", lib.lengthOfLastWord("Hello World"))
    print ("Answer No. 3: ", lib.lengthOfLastWord("luffy is still joyboy"))
    print ("Answer No. 4: ", lib.lengthOfLastWord("luffy"))
    print ("Answer No. 5: ", lib.lengthOfLastWord(""))

def printingLongestCommonPrefix():
    lib = ListBundle01()
    print ("[ Longest Common Prefix ]")
    print ("Answer No. 1, type 1: ", lib.longestCommonPrefix_1(["flower","flow","flight"]))
    print ("Answer No. 2, type 1: ", lib.longestCommonPrefix_1(["dog","racecar","car"]))
    print ("Answer No. 3, type 1: ", lib.longestCommonPrefix_1(["car"]))
    print ("Answer No. 4, type 1: ", lib.longestCommonPrefix_1([""]))
    print ("Answer No. 1, type 2: ", lib.longestCommonPrefix_2(["flower","flow","flight"]))
    print ("Answer No. 2, type 2: ", lib.longestCommonPrefix_2(["dog","racecar","car"]))
    print ("Answer No. 3, type 2: ", lib.longestCommonPrefix_2(["car"]))
    print ("Answer No. 4, type 2: ", lib.longestCommonPrefix_2([""]))

def printingTopKFreqElement():
    lib = ListBundle01()
    print ("[ Top K Frequenct Element ]")
    print (" Answer 1, type 1 ", lib.topKFrequent_1([1,1,1,2,2,3],2))
    print (" Answer 2, type 1 ", lib.topKFrequent_1([1],1))

def printingEncodeDecode():
    lib = ListBundle01()
    print ("[ Encode / Decode Strings ]")
    a = ["neet","code","love","you"]
    s = lib.encode(a)
    print ("Answer 1 (encode): ", s)
    b = lib.decode(s)
    print ("Answer 1 (decode): ", b)

def printingArrayExceptSelf():
    lib = ListBundle01()
    print ("[ 238. Array Except Self ]")
    nums = [1,2,3,4]
    print ("Answer #1: ", lib.productExceptSelf_1(nums))
    print ("Answer #2: ", lib.productExceptSelf_2(nums))

def printingPascalTriangle():
    lib = ListBundle01()
    print ("[ Pascal's Triangle ]")
    print ("Answer #1: ", lib.generatePascalTriangle(1))
    print ("Answer #2: ", lib.generatePascalTriangle(2))
    print ("Answer #3: ", lib.generatePascalTriangle(3))
    print ("Answer #4: ", lib.generatePascalTriangle(4))
    print ("Answer #5: ", lib.generatePascalTriangle(5))
    print ("Answer #5: ", lib.generatePascalTriangle(6))

def printingUniqueEmailAddress():
    lib = ListBundle01()
    print (" [ Unique Email Address ]")
    print ("Answer #1: ", lib.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
    print ("Answer #2: ", lib.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))    

def printingIsomorphicString():
    lib = StringBundle01()
    print (" [ Isomorphic String ] ")
    print (" Answer #1: ", lib.is_isomorphic("aab", "xxy"))

def printingCanPlaceFlowers():
    lib = ListBundle01()
    print (" [ 605. Can Place Flowers ]")
    print ("Answer #1: ", lib.canPlaceFlowers([1,0,0,0,1], 1))
    print ("Answer #2: ", lib.canPlaceFlowers([1,0,0,0,1], 2))
    print ("Answer #3: ", lib.canPlaceFlowers([1,0,0,0,0,0,1], 2))

def printingMajorityElement():
    lib = ListBundle01()
    print (" [ 169. Majority Element ]")
    print ("Answer #1 type 1: ", lib.majorityElement_1([3,2,3]))
    print ("Answer #2 type 1: ", lib.majorityElement_1([2,2,1,1,1,2,2]))
    print ("Answer #1 type 2: ", lib.majorityElement_2([3,2,3]))
    print ("Answer #2 type 2: ", lib.majorityElement_2([2,2,1,1,1,2,2]))

def printingNextGreaterElement():
    lib = ListBundle01()
    print (" [ 496. Next Greater Element ]")
    print ("Answer #1: type:1", lib.nextGreaterElement_1([4,1,2], [1,3,4,2]))
    print ("Answer #2: type:1", lib.nextGreaterElement_1([2,4], [1,2,3,4]))
    print ("Answer #2: type:1", lib.nextGreaterElement_1([1,3,5,2,4], [6,5,4,3,2,1,7]))
    print ("Answer #1: type:2 ", lib.nextGreaterElement_2([4,1,2], [1,3,4,2]))
    print ("Answer #2: type:2", lib.nextGreaterElement_2([2,4], [1,2,3,4]))
    print ("Answer #2: type:2", lib.nextGreaterElement_2([1,3,5,2,4], [6,5,4,3,2,1,7]))
    print ("Answer #1: type:3 ", lib.nextGreaterElement_3([4,1,2], [1,3,4,2]))
    print ("Answer #2: type:3", lib.nextGreaterElement_3([2,4], [1,2,3,4]))
    print ("Answer #2: type:3", lib.nextGreaterElement_3([1,3,5,2,4], [6,5,4,3,2,1,7]))

def printingFindPivotIndex():
    lib = ListBundle01()
    print (" [ 724. Find Pivot Index ]")
    print ("Answer #1: ", lib.pivotIndex([1,7,3,6,5,6]))
    print ("Answer #2: ", lib.pivotIndex([1,2,3]))
    print ("Answer #3: ", lib.pivotIndex([2,1,-1]))
    print ("Answer #3: ", lib.pivotIndex([-1,-1,-1,-1,-1,-1]))

def printingSumNumpyArrayRange():
    lib = ListBundle01()
    print (" [ 303. Range Sum Query ]")
    print ("Answer #1: ", lib.sumRange([-2, 0, 3, -5, 2, -1],0,2))
    print ("Answer #2: ", lib.sumRange([-2, 0, 3, -5, 2, -1],2,5))
    print ("Answer #3: ", lib.sumRange([-2, 0, 3, -5, 2, -1],0,5))

def printingFindAllNumsDisappeared():
    lib = ListBundle01()
    print (" [ 448. Find All Numbers Disappeared in an Array ]")
    print ("Answer #1: type:1 ",  lib.findDisappearedNumbers_1([4,3,2,7,8,2,3,1]))
    print ("Answer #1: type:2 ",  lib.findDisappearedNumbers_2([4,3,2,7,8,2,3,1]))

def printingMaxNumberBallons():
    lib = ListBundle01()    
    print (" [ 1189. Maximum Number of Ballons ]")
    print ("Answer #1: ",  lib.maxNumberOfBalloons_2("nlaebolko"))
    print ("Answer #2:",  lib.maxNumberOfBalloons_2("loonbalxballpoon"))
    print ("Answer #3:",  lib.maxNumberOfBalloons_2("leetcode"))

def printingWordPattern():
    lib = ListBundle01()    
    print (" [ 290. Word Pattern ]")
    print ("Answer #1: ",  lib.wordPattern(pattern = "abba", s = "dog cat cat dog"))
    print ("Answer #2: ",  lib.wordPattern(pattern = "abba", s = "dog cat cat fish"))
    print ("Answer #3: ",  lib.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))

def printingHashSet():
    print (" [ 705. Design HashSet ]")
    myHashSet = MyHashSet();
    myHashSet.add(1)        # set = [1]
    myHashSet.add(2)        # set = [1, 2]
    myHashSet.contains(1)   # return True
    myHashSet.contains(3)   # return False, (not found)
    myHashSet.add(2)        # set = [1, 2]
    myHashSet.contains(2)   # return True
    myHashSet.remove(2)     # set = [1]
    myHashSet.contains(2)   # return False, (already removed)

def printingHashMap():
    print (" [ 705. Design HashMap ]")
    myHashMap = MyHashMap();
    myHashMap.put(1, 1)     # The map is now [[1,1]]
    myHashMap.put(2, 2)     # The map is now [[1,1], [2,2]]
    myHashMap.get(1)        # return 1, The map is now [[1,1], [2,2]]
    myHashMap.get(3)        # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
    myHashMap.put(2, 1)     # The map is now [[1,1], [2,1]] (i.e., update the existing value)
    myHashMap.get(2)        # return 1, The map is now [[1,1], [2,1]]
    myHashMap.remove(2)     # remove the mapping for 2, The map is now [[1,1]]
    myHashMap.get(2)        # return -1 (i.e., not found), The map is now [[1,1]]    

def printingTwoIntSumII():
    lib = ListBundle01()  
    print (" [ 167. Two Integer Sum II ]")
    print (" Answer:1 type 1",  lib.twoSumII_1([1,2,3,4],3))
    print (" Answer:2 type 2",  lib.twoSumII_2([1,2,3,4],3))

def printingLongestConsecSeq():
    lib = ListBundle01()  
    print (" [ 128. Longest Consecutive Sequence ]")
    print (" Answer 1 type 1: ",  lib.longestConsecutive([2,20,4,10,3,4,5]))
    print (" Answer 2 type 1: ",  lib.longestConsecutive([0,3,2,5,4,6,1,1]))
    print (" Answer 3 type 1: ", lib.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))

def printingTrappingRainWater():
    lib = ListBundle01()  
    print (" [ 42. Trapping Rain Water ]")
    print (" Answer 1 type 1: ",  lib.trap([0,2,0,3,1,0,1,3,2,1]))

def printingMaxProfitSellingStock():
    lib = ListBundle01()
    print (" [ 121. Best Time to Buy and Sell Stock ]")
    print ("Answer 1: ", lib.maxProfit([10,1,5,6,7,1]))
    print ("Answer 2: ", lib.maxProfit([10,8,7,5,2]))
    
def printingLongestSubstrWithoutRepChars():
    lib = StringBundle01()
    print (" [ 3. Longest sub string Without Repeat Characters ]")
    print ("Answer 1, type 1: ", lib.lengthOfLongestSubstring_1("zxyzxyz"))
    print ("Answer 2, type 1: ", lib.lengthOfLongestSubstring_1("xxxx"))
    print ("Answer 3, type 1: ", lib.lengthOfLongestSubstring_1("au"))
    print ("-")
    print ("Answer 1, type 2: ", lib.lengthOfLongestSubstring_2("zxyzxyz"))
    print ("Answer 2, type 2: ", lib.lengthOfLongestSubstring_2("xxxx"))
    print ("Answer 3, type 2: ", lib.lengthOfLongestSubstring_2("au"))
    print ("Answer 4, type 2: ", lib.lengthOfLongestSubstring_2("pwwkew"))

def printingLongestRepCharReplacement():
    lib = StringBundle01()
    print (" [ 424. Longest Repeating Character Replacement ]")
    print ("Answer 1, ", lib.characterReplacement("XYYX",2))
    print ("Answer 2, ", lib.characterReplacement("AAABABB",1))

def printingValidParentheses():
    lib = StringBundle01()
    print (" [ 20. Valid Parentheses ]")
    print ("Answer 1, ", lib.isValidParentheses("[]"))
    print ("Answer 2, ", lib.isValidParentheses("([{}])"))
    print ("Answer 3, ", lib.isValidParentheses("[(])"))
    print ("Answer 4, ", lib.isValidParentheses("]"))
    print ("Answer 4, ", lib.isValidParentheses("]]"))

def printingMinStack():
    minStack = MinStack()
    print (" [ 155. Minimum Stack ]")
    minStack.push(1);
    minStack.push(2);
    minStack.push(0);
    minStack.print()
    print(minStack.getMin()); # return 0
    minStack.pop();
    print(minStack.top());    # return 2
    print(minStack.getMin()); # return 1
    minStack.print()

    #second  ["MinStack", "push", 10, "pop", "push", 20, "top", "push", -20, "getMin"]
    minStack = MinStack()
    print(minStack.getMin())
    minStack.push(10)
    print(minStack.pop())
    minStack.push(20)
    print(minStack.pop())
    minStack.push(-20)
    minStack.print()
    print(minStack.getMin())

    #second  ["MinStack", "push", -2, "push", -2, "push", -3, "push", -3, "getMin", "pop", "getMin"]
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(-2)
    minStack.push(-3)
    minStack.push(-3)    
    minStack.print()
    minStack.pop()
    print(minStack.getMin())

def printingGenerateParentheses():
    lib = StringBundle01()
    print (" [ 22. Generate Parentheses ]")
    print ("Answer 1, ", lib.generateParenthesis(1))
    print ("Answer 1, ", lib.generateParenthesis(3))

def printingDailyTemperatures():
    lib = ListBundle01()
    print (" [ 739. Daily Temperatures ]")
    print ("Answer 1, ", lib.dailyTemperatures([30,38,30,36,35,40,28]))
    print ("Answer 2, ", lib.dailyTemperatures([22,21,20]))

def printingBinarySearch():
    lib = ListBundle01()
    print (" [ 704. Binary Search ]")
    print ("Answer 1:", lib.binarySearch([-1,0,2,4,6,8],4))
    print ("Answer 2:", lib.binarySearch([-1,0,2,4,6,8],3))

def printingSearch2dMatrix():
    lib = MatrixBundle01()
    print (" [ 74. Search a 2D Matrix ]")
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    print ("Answer 1:", lib.searchMatrix(matrix,10))
    print ("Answer 2:", lib.searchMatrix(matrix,15))

def printingEvaluateReversePolishNotation():
    lib = ListBundle01()
    print (" [ 150. Evaluate Reverse Polish Notation ]")
    tokens = ["1","2","+","3","*","4","-"]
    print ("Answer 1:", lib.evalRPN(tokens))

def printingPermutationString():
    lib = StringBundle01()
    print (" [ 567. Permutation in String ]")
    print ("Answer 1, ", lib.checkInclusion_1(s1 = "abc", s2 = "lecabee"))
    print ("Answer 1, ", lib.checkInclusion_1(s1 = "abc", s2 = "lecaabee"))
    print ("Answer 1, type 2", lib.checkInclusion_2(s1 = "abc", s2 = "lecabee"))
    print ("Answer 1, type 2", lib.checkInclusion_2(s1 = "abc", s2 = "lecaabee"))    
    print ("Answer 1, type 2", lib.checkInclusion_2(s1 = "adc", s2 = "dcda"))    
    print ("Answer 1, type 3", lib.checkInclusion_3(s1 = "abc", s2 = "lecabee"))
    print ("Answer 1, type 3", lib.checkInclusion_3(s1 = "abc", s2 = "lecaabee"))    
    print ("Answer 1, type 3", lib.checkInclusion_3(s1 = "adc", s2 = "dcda")) 

def printingMinimumWindowSubstring():
    lib = StringBundle01()
    print (" [ 000. Minimum Window Substring ]")
    print ("Answer 1, ",lib.minWindow(s = "OUZODYXAZV", t = "XYZ"))
    print ("Answer 2, ",lib.minWindow(s = "xyz", t = "xyz"))
    print ("Answer 3, ",lib.minWindow(s = "x", t = "xy"))
    print ("Answer 4, ",lib.minWindow(s = "t", t = "aa"))
    print ("Answer 5, ",lib.minWindow(s = "aa", t = "aa"))


def menu():
    print("Menu Practice Python No. 1")
    print("1. Two Sum (LC#1)                         21. Maximum Number of Ballons (LC#1189)")
    print("2. Contains Duplicate (LC#217)            22. Word Patten (LC#290)")
    print("3. Valid Anagram (LC#242)                 23. Design HashSet (LC#705)")
    print("4. Group Anagram (LC#49)                  24. Design HashMap (LC#706)")
    print("5. Replace Elements (LC#1299)             25. Two Integer Sum II (LC#167)")
    print("6. Is Sequence (LC#392)                   26. Longest Consecutive Sequence (LC#128)")
    print("7. Length of Last Word (LC#58)            27. Trapping Rain Water (LC#42)")
    print("8. Longest Common prefix (lc#14)          28. Best Time to Buy and Sell Stock (LC#121)")
    print("9. Top K Frequent Element (LC#347)        29. Longest substr Without Rep Chars(LC#3)")
    print("10. Encode and Decode String (neetcode)   30. Longest Repeat Char Replacement (LC#424)")
    print("11. Product of Array Except Self (LC#238) 31. Valid Parentheses (LC#20)")
    print("12. Pascal's Triangle (LC#118)            32. Minimum Stack (LC#155)")
    print("13. Unique Email Addresses (LC#929)       33. Generate Parentheses (LC#22)")
    print("14. Isomorphic String (LC#205)            34. Daily Temperatures (LC#739) *need review ")
    print("15. Can Place Flowers (LC#605)            35. Binary Search (LC#704)")
    print("16. Majority Element (LC#169)             36. Search a 2D Matrix (LC#74)")
    print("17. Next Greater Element I (LC#496)       37. Evaluate Reverse Polish Notation (LC#150)")
    print("18. Find Pivot Index (LC#724)             38. Permutation in String (LC#567)")
    print("19. Sum Numpy Array Range (LC#303)        39. Minimum Window Substring *need review ")
    print("20. Find All Numbers Disappeared (LC#448) 40. ")

    opc = int(input("Enter Option? "))
    match opc:
        case 1: printingSumTwo()
        case 2: printingContainsDuplicate()
        case 3: printingValidAnagram()
        case 4: printingGroupAnagram()
        case 5: printingReplaceElements()
        case 6: printingIsSequence()
        case 7: printingLengthLastWord()
        case 8: printingLongestCommonPrefix()
        case 9: printingTopKFreqElement()
        case 10: printingEncodeDecode()
        case 11: printingArrayExceptSelf()
        case 12: printingPascalTriangle()
        case 13: printingUniqueEmailAddress()
        case 14: printingIsomorphicString()
        case 15: printingCanPlaceFlowers()
        case 16: printingMajorityElement()
        case 17: printingNextGreaterElement()
        case 18: printingFindPivotIndex()
        case 19: printingSumNumpyArrayRange()
        case 20: printingFindAllNumsDisappeared()
        case 21: printingMaxNumberBallons()
        case 22: printingWordPattern()
        case 23: printingHashSet()
        case 24: printingHashMap()
        case 25: printingTwoIntSumII()
        case 26: printingLongestConsecSeq()
        case 27: printingTrappingRainWater()
        case 28: printingMaxProfitSellingStock()
        case 29: printingLongestSubstrWithoutRepChars()
        case 30: printingLongestRepCharReplacement()
        case 31: printingValidParentheses()
        case 32: printingMinStack()
        case 33: printingGenerateParentheses()
        case 34: printingDailyTemperatures()
        case 35: printingBinarySearch()
        case 36: printingSearch2dMatrix()
        case 37: printingEvaluateReversePolishNotation()
        case 38: printingPermutationString()
        case 39: printingMinimumWindowSubstring()
        case _: print("Error, option not recognized")

menu()
