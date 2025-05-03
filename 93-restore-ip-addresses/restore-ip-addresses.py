class Solution:
    def isValid(self,s):
        if s == "0":
            return True
        elif int(s) > 255 or int(s) < 0 or s.startswith("0"):
            return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []
        res = []
        self.backtrack(s,0,0,[],res)
        return res

    def backtrack(self,s,start,parts,path,res):
        if parts == 4 and start == len(s):
            res.append(".".join(path))
            return res
        
        if parts > 4:
            return

        for length in range(1,4):
            if start + length > len(s):
                break
            segment = s[start:start+length]
            if self.isValid(segment):
                self.backtrack(s,start+length, parts+1,path+[segment],res)
            
        
            
        
        
        