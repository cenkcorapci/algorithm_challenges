from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        else:
            adjacency = self.dfs(node)
            start = node.val


    def dfs(self, curnode: Optional['Node']) -> dict[int, List[int]]:
        if curnode is None:
            return dict()
        stack = []
        adjacency = dict[int, List[int]]()

        for neighbor in curnode.neighbors:
            stack.append(neighbor)
        adjacency[curnode.val] = [neighbor.val for neighbor in curnode.neighbors]
        while stack:
            node = stack.pop()
            if node.val not in adjacency:
                adjacency[node.val] = [neighbor.val for neighbor in node.neighbors]
                for neighbor in node.neighbors:
                    stack.append(neighbor)
        return adjacency
