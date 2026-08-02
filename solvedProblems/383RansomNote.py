class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        #key is the letter, value is the running total of that letter
        #ransom increments, magazine decrements
        ransomDict = {}

        for i in ransomNote:
            if i in ransomDict:
                ransomDict[i] += 1
            else:
                ransomDict[i] = 1

        for i in magazine:
            if i in ransomDict:
                ransomDict[i] -= 1                    

        for j in ransomDict:
            if ransomDict[j] > 0:
                return False
        return True

print(Solution.canConstruct(Solution, "aaa", "bcaaa"))