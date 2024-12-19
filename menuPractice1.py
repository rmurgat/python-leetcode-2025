from solutions.ListBunble01 import *

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
    print ("[ Array Except Self ]")
    nums = [1,2,3,4]
    print ("Answer #1: ", lib.productExceptSelf(nums))


def menu():
    print("Menu Practice Python No. 1")
    print("1. Two Sum (LC#1)")
    print("2. Contains Duplicate (LC#217)")
    print("3. Valid Anagram (LC#242)")
    print("4. Group Anagram (LC#49)")
    print("5. Replace Elements (LC#1299)")
    print("6. Is Sequence (LC#392)")
    print("7. Length of Last Word (LC#58)")
    print("8. Longest Common prefix (lc#14)")
    print("9. Top K Frequent Element (LC#347)")
    print("10. Encode and Decode String (neetcode)")
    print("11. Product of Array Except Self (LC#238)")
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
        case _: print("Error, option not recognized")

menu()
