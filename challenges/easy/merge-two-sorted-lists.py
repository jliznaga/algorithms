# Definition for singly-linked list.
# https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Optional

def convert_list_to_node(l: list):
    res = ListNode()
    i = 0
    while i < len(l) - 1:
        res = ListNode(l[i], ListNode(l[i + 1]))
        i+=1
    
    return res


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        head1 = list1
        head2 = list2
        res = ListNode()

        if head1.val < head2.val:
            res = head1
            res.next = head2
            res = head2
        else:
            res = head2
            res.next = head1
            res = head1

        list1 = list1.next
        list2 = list2.next

        while list1.next != None and list2.next != None:
            if list1.val < list2.val:
                res = list1
                res.next = list2
                res = list2
            else:
                res = list2
                res.next = list1
                res = list1

            list1 = list1.next
            list2 = list2.next

        return res


obj = Solution()
print(obj.mergeTwoLists(convert_list_to_node([1]), convert_list_to_node([2,3,4])))