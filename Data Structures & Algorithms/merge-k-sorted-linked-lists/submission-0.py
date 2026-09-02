# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for lst in lists:
            while lst:
                heapq.heappush(min_heap, lst.val)
                lst = lst.next
        
        dummy = ListNode(0)
        merge = dummy

        while min_heap:
            merge.next = ListNode(heapq.heappop(min_heap))
            merge = merge.next

        return dummy.next