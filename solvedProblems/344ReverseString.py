class Solution:
    def reverseString(self, s: list[str]) -> None:
        self.helper(self, s, 0)
        print(s)

    def helper(self, s, index):
        temp = ""
        if index >= (len(s) >> 1):
            return
        self.helper(self, s, index + 1)
        temp = s[index]
        s[index] = s[(index * -1) - 1]
        s[(index * -1) - 1] = temp

print(Solution.reverseString(Solution,["a","b","c","d","e"]))