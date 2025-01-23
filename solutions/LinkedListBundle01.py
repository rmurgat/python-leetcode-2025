from typing import List, Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random         

class LinkedListBundle01:

    def createListNode(self, lst: list)-> Optional[ListNode]:
        if not lst: return None
        head = ListNode()
        r = head
        for i in range(0, len(lst)):
            r.val = lst[i]
            if i < len(lst)-1:
                r.next = ListNode()
                r = r.next
        return head

    def printListNode(self, head: Optional[ListNode]):
        print ("[", end="")
        while head:
            print (head.val, ", ", end="")
            head = head.next
        print ("]")

    def convertListNode2List(self, head: Optional[ListNode]):
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None        
        while head:
            next_ = head.next
            head.next = last
            last = head
            head = next_
        return last
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: return list2
        if list2 is None: return list1
        ans = h3 = ListNode(-1)
        while list1 and list2:
            if list1.val <= list2.val:
                h3.next = list1
                if list1.next:
                    list1 = list1.next
                else:
                    list1.next = list2
                    break
            else:
                h3.next = list2
                if list2.next:
                    list2 = list2.next
                else:
                    list2.next = list1
                    break
            h3 = h3.next
        return ans.next
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        memo = []
        while head:
            if head in memo: return True
            memo.append(head)
            head = head.next
        return False
    
    def reorderList(self, head: Optional[ListNode]) -> None:

        original = head
        #splitting ListNode in two half
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        last = None
        head2 = slow.next
        slow.next = None
        while head2:
            next_ = head2.next
            head2.next = last
            last = head2
            head2 = next_
        head2 = last

        # merging two halfs
        while head and head2:
            next_ = head.next
            next2_ = head2.next
            head.next = head2
            head2.next = next_
            head = next_
            head2 = next2_

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def backtracking(node: Optional[ListNode]) ->  list:
            if node is None: return [None, 0]
            ans = backtracking(node.next)
            node.next = ans[0] 
            cnt = ans[1] + 1
            if cnt == n:
                node = node.next
            return [node, cnt]
        return backtracking(head)[0]