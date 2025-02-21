class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        track = {}
        for i in range(len(temp)):
            if temp[i] not in track:
                track[temp[i]] = i

        res = []
        for num in nums:
            res.append(track[num])
        return res
