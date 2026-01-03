# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # reorder list to be first, last, second, second to last
        # we put all nodes in a stack
        # we use a double ended queue
        # we pop from left to get first 
        # we pop from right ot get last
        # and go back and fourth

        # now how do we rearrange ll like this
        stack = deque()
        curr = head

        while curr != None:
            stack.append(curr)
            curr = curr.next

        # now we have stack
        # take from left and right
        switch = False
        prev = None
        while stack:
            if not switch:
                node = stack.popleft()
                
            else:
                node = stack.pop()
                
            switch = not switch
            node.next = None

            if prev:
                prev.next = node
            prev = node

        prev.next = None
            

        

