from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            total = node.val + left_sum + right_sum
            freq[total] += 1

            return total

        dfs(root)

        max_freq = max(freq.values())

        ans = []

        for subtree_sum, count in freq.items():
            if count == max_freq:
                ans.append(subtree_sum)

        return ans