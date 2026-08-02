class Solution:
    def myPow(self, x: float, n: int) -> float:
        #kept prime factor function because i like it and made it while
        #trying to solve the problem on my own, after looking at solutions
        #its not usefull but i still i like it

        return self.powRecur(self, x, n)

    def powRecur(self, x, n):

        if n == 1:
            return x
        if not n:
            return 1
        if n < 0:
            answer = 1 / self.powRecur(self, x, -n)
            return answer
        if n % 2:
            answer = x * self.powRecur(self, x, n-1)
            return answer
        answer = self.powRecur(self, x*x, n >> 1)
        return answer

    def findPrimeFactors(self, n: int, primeFactors: list[int]):
        
        for i in range(2, int(n)):
            if n % i == 0:
                primeFactors.append(i)
                return self.findPrimeFactors(self, (n/i), primeFactors)

        primeFactors.append(int(n))
        return primeFactors

print(Solution.myPow(Solution, 2.0, -200000000))
#print(Solution.findPrimeFactors(Solution, 8, []))