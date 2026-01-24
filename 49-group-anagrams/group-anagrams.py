class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for word in strs:
            sortedWord = "".join(sorted(word))
            seen[sortedWord].append(word)
        return list(seen.values())
