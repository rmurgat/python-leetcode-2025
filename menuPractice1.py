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



def menu():
    print("Menu Practice Python No. 1")
    print("1. Two Sum (LC#1)")
    print("2. Contains Duplicate (LC#217)")
    print("3. Valid Anagram (LC#242)")
    opc = int(input("Enter Option?"))
    match opc:
        case 1: printingSumTwo()
        case 2: printingContainsDuplicate()
        case 3: printingValidAnagram()
        case _: print("Error, option not recognized")

menu()
