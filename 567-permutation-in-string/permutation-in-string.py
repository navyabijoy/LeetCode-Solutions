class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        slow=0
        fast=0
        s1_count= Counter(s1)
        while fast < len(s2):
            if s2[fast] in s1_count:
                s1_count[s2[fast]] -= 1
            if all(val == 0 for val in s1_count.values()) and fast-slow+1 == len(s1):
                return True
            if fast-slow+1 == len(s1):
                if s2[slow] in s1_count:
                    s1_count[s2[slow]] += 1
                slow +=1
            fast +=1 
        return False
