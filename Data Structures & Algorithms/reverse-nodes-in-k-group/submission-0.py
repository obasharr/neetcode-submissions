# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr = head
        ktail = None
        new_head = None

        while ptr:
            count = 0
            ptr = head

            while count < k and ptr:
                ptr = ptr.next
                count += 1

            if count == k:
                rev_head = self.reverseLinkedList(head, k)

                if not new_head:
                    new_head = rev_head

                if ktail:
                    ktail.next = rev_head
                
                ktail = head
                head = ptr
        if ktail:
            ktail.next = head
        
        return head if not new_head else new_head

    def reverseLinkedList(self, head: ListNode, k: int) -> ListNode:
        new_head = None
        ptr = head

        while k > 0:
            next_node = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr = next_node
            k -= 1
        
        return new_head

        


