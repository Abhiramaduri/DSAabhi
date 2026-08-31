# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_distance = float('inf')
        first_crit_index = -1
        prev_crit_index = -1
        index = 1
        
        prev = head
        curr = head.next
        
        while curr and curr.next:
            is_local_max = curr.val > prev.val and curr.val > curr.next.val
            is_local_min = curr.val < prev.val and curr.val < curr.next.val
            
            if is_local_max or is_local_min:
                if first_crit_index == -1:
                    first_crit_index = index
                if prev_crit_index != -1:
                    min_distance = min(min_distance, index - prev_crit_index)
                prev_crit_index = index
                
            prev = curr
            curr = curr.next
            index += 1
            
        if min_distance == float('inf'):
            return [-1, -1]
            
        max_distance = prev_crit_index - first_crit_index
        return [min_distance, max_distance]

        