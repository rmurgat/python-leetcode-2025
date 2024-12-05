from solutions.ListBunble01 import *

def printingSumTwo():
    lib = ListBundle01()
    print ("Sum Two: ", lib.twoSum([2,7,11,15],9))

def menu():
    print("Menu Practice Python No. 1")
    print("1. Two Sum (LC#1)")
    opc = int(input("Enter Option?"))
    match opc:
        case 1: printingSumTwo()
        case _: print("Error, option not recognized")

menu()
