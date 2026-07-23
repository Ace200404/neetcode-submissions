class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)==0:
            return True
        if len(s)==1:
            return False

        stack =[]
        par_key={')': '(', '}': '{', ']': '['}

        for i in s:
            if i in par_key:
                if stack and stack[-1] == par_key[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if len(stack)==0 else False
                