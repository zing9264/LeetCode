class Solution:
    def defangIPaddr(self, address: str) -> str:
        output=address.replace('.', '[.]')
        return output

if __name__ == "__main__":

    s = ["1.1.1.1","255.100.50.0"]
    ans = Solution()
    for i in s:
        print("----------"+i+"-----------\n"+ans.defangIPaddr(i))
