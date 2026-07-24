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
            if (not star) or (star and (starChar != sStack[-1] and starChar != ".")):
                if len(pStack) >= 2:
                    if pStack[-2] == "*":
                        star = True
                        starChar = pStack[-1]
                        pStack.pop()
                        pStack.pop()
                        if not bool(pStack):
                            continue
                    else:
                        star = False
                else:
                    star = False
            print("star " + str(star))
            if star:    # there is a star
                if starChar == "." or starChar == sStack[-1]:
                    if pStack[-1] == "." or pStack[-1] == sStack[-1]:
                        sStack.pop()
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

print(Solution.isMatch(Solution, "aaqwbb", ".*aa.*bb"))