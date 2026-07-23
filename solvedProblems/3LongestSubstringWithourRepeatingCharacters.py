class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        LSSLength = 0

        for i in range(0,len(s)):
            seenLetters = []
            currentSSLength = 0

            for j in range(i,len(s)):
                if Solution.containsChar(s[j], seenLetters):
                    break
                else:
                    seenLetters.append(s[j])
                    currentSSLength += 1

            if currentSSLength > LSSLength:
                LSSLength = currentSSLength

        return LSSLength

    def containsChar(c: str, l: list) -> bool:
        for i in range (0, len(l)):
            if c == l[i]:
                return True
        return False

print(Solution.lengthOfLongestSubstring(Solution, "abcabcbb"))