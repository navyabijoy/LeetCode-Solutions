class Solution:
    def backtrack(self,pos,hours,minutes,enabled,result):
        if enabled == 0:
            if hours <= 11 and minutes <= 59:
                time = f"{hours}:{'0' if minutes < 10 else ''}{minutes}"
                result.append(time)
            return 

        for i in range(pos,10):
            h,m = hours, minutes
            if i <= 3:
                hours += int(pow(2,i))
            else:
                minutes += int(pow(2, i-4))
            self.backtrack(i+1,hours,minutes,enabled-1,result)
            hours, minutes = h,m

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        self.backtrack(0,0,0,turnedOn, res)
        return res
            