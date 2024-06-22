from typing import List

"""
Time complexity: O(N)
Space complextiy: O(1)
"""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)   