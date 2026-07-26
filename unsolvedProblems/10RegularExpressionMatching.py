class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        sStack = []
        pStack = []
        star = False
        starChar = ""

        #pushing s onto stack in reverse order
        for i in range(0,len(s)):
            sStack.append(s[(i*-1)-1])

        #pushing p onto stack in reverse order
        for i in range(0,len(p)):
            pStack.append(p[(i*-1)-1])

        print(sStack)
        print(pStack)

        while bool(sStack) and bool(pStack):
            # 1 char look ahead to find *
            if len(pStack) >= 2:
                if pStack[-2] == "*":   # look ahead is *
                    star = True
                    if sStack[-1] == pStack[-1]:
                        if starChar != ".":
                            starChar = pStack[-1]
                        else:
                            starChar = "."
                    pStack.pop()
                    pStack.pop()
                    if not bool(pStack):
                        continue
                # look ahead is not * and starChar is not . and
                # starChar does not match top of sStack
                elif (starChar != ".") and (starChar != sStack[-1]):
                    star = False
                    starChar = ""
            # pStack is less than 2 long and starChar is not . and
            # starChar does not match top of sStack
            elif (starChar != ".") and (starChar != sStack[-1]):
                star = False
                starChar = ""

            print("star " + str(star))
            print("star char " + str(starChar))

            if star:    # there is a star
                if starChar == "." or starChar == sStack[-1]:
                    if pStack[-1] == "." or pStack[-1] == sStack[-1]:
                        sStack.pop()
                        if len(pStack) >= 2:
                            if pStack[-2] != "*":
                                pStack.pop()
                    else:
                        sStack.pop()
            #no star and top of stacks match
            elif sStack[-1] == pStack[-1] or pStack[-1] == ".":
                sStack.pop()
                pStack.pop()
            else: #no star and top of stacks dont match
                return False

            print("sStack " + str(sStack))
            print("pStack " + str(pStack))
            print("--------------------")

        # pStack is empty and sStack is not empty
        if (not bool(pStack)) and (bool(sStack)):
            if star:
                if starChar == "." or starChar == sStack[-1]:
                    sStack.pop()
                else:
                    return False
            else:
                return False
        # pStack is not empty and sStack is empty
        if bool(pStack) and (not bool(sStack)):
            return False

        return True

print(Solution.isMatch(Solution, "abcda", ".*a"))