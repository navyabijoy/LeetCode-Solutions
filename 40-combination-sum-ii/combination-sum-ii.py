class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(index, res, total):
            if total == target:
                ans.append(res[:])
                return

            if index == len(candidates) or total > target:
                return

            res.append(candidates[index])
            backtrack(index + 1, res, total + candidates[index])
            res.pop()
            while (
                index + 1 < len(candidates) and candidates[index] == candidates[index + 1]
            ):
                index += 1
            backtrack(index + 1, res, total)

        backtrack(0, [], 0)
        return sorted(ans)
