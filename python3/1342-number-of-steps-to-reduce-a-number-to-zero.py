"""
Time complexity: O(Log(N))
Space complextiy: O(1)
"""
class Solution:
    def numberOfSteps(self, num: int) -> int:
        q = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            q += 1
        return q