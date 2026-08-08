class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        sDict = {}
        tDict = {}

        for i in range(0,len(s)):
            if s[i] in sDict:
                if sDict[s[i]] != t[i]:
                    return False
            else:
                sDict[s[i]] = t[i]

        for i in range(0,len(t)):
            if t[i] in tDict:
                if tDict[t[i]] != s[i]:
                    return False
            else:
                tDict[t[i]] = s[i]

        return True

print(Solution.isIsomorphic(Solution, "egg", "add"))
print(Solution.isIsomorphic(Solution, "foo", "bar"))
print(Solution.isIsomorphic(Solution, "bbbaaaba", "aaabbbba"))
print(Solution.isIsomorphic(Solution, "badc", "baba"))
