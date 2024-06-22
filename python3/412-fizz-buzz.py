"""
Time complexity: O(N)
Space complextiy: O(1)
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        q = []
        for i in range(1, n + 1):
            s = ""
            if i % 3 == 0: s += "Fizz"
            if i % 5 == 0: s += "Buzz"
            q.append(str(i) if not s else s)
        return q