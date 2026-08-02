class Solution:
    def fizzBuzz(self, n: int) -> list[str]:

        answer = []
        threeCount = 1
        fiveCount = 1

        for i in range(1,n+1):
            if threeCount == 3:
                threeCount = 0
                if fiveCount == 5:
                    fiveCount = 0
                    answer.append("FizzBuzz")
                else:
                    answer.append("Fizz")
            elif fiveCount == 5:
                fiveCount = 0
                answer.append("Buzz")
            else:
                answer.append(str(i))
            threeCount += 1
            fiveCount += 1

        return answer

print(Solution.fizzBuzz(Solution, 3))
        