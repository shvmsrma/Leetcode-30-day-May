class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        rem = k
        for n in num:
            while rem and stack and stack[-1] > n:
                stack.pop()
                rem = rem - 1
            stack.append(n)
        answer = "".join(stack[0:len(num)-k]).lstrip("0")
        if len(answer):
            return answer
        else:
            return "0"
               
        
