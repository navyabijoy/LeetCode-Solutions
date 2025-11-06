class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack =[]
        for ch in s:
            if stack and stack[-1][0] == ch:
                char, count = stack.pop()
                count += 1
                if count < k:
                    stack.append((char, count))
            else:
                stack.append((ch,1))
        
        res = []
        for char, cnt in stack:
            res.append(char * cnt)
        
        return "".join(res)