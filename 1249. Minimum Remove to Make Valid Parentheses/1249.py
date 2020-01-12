class Solution:
    def __init__(self):
        pass

    def minRemoveToMakeValid(self, s: str) -> str:
        remain_left = 0
        output = ""
        addstate= True
        for i in s:
            if (i) == '(':
                remain_left += 1
                addstate=True
            elif (i) == ')':
                if (remain_left > 0):
                    remain_left -= 1
                    addstate = True
                else:
                    addstate = False

            if addstate == True:
                output += i
            addstate = True

        k = output[::-1].replace("(", "", remain_left)
        output = k[::-1]
        
        return output


if __name__ == "__main__":

    s = ["lee(t(c)o)de)","a)b(c)d","))(((","))((((((((((())))))))","(a(b(c)d)","cccccasd( asfd)"]
    ans = Solution()
    for i in s:
        print("----------"+i+"-----------\n"+ans.minRemoveToMakeValid(i))
