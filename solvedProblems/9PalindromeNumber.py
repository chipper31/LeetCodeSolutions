class Solution:
    def isPalindrome(self, x: int) -> bool:

        text = str(x)
        textLength = len(text)

        for i in range(0, textLength // 2):
            if (text[i]!=text[textLength-i-1]):
                return False

        return True
    
#print(Solution.isPalindrome(Solution, 121))