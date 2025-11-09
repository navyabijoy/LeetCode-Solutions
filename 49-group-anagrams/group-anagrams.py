class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        hashMap = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            hashMap[key].append(word)

        return list(hashMap.values())
