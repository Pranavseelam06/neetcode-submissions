"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        my_dict = dict()
        new_head = None
        cur = head
        while cur:
            my_dict[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            current_node = my_dict[cur]
            if cur.next is not None:
                current_node.next = my_dict[cur.next]
            if cur.random is not None:
                current_node.random = my_dict[cur.random]
            my_dict[cur] = current_node
            cur = cur.next
        return my_dict[head]
        