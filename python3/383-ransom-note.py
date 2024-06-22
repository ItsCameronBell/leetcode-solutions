"""
Time complexity: 
Space complextiy: 
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for r in ransomNote:
            if r in magazine:
                magazine = magazine.replace(r, "", 1) 
            else: return False
        return True
