class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        final = []
        ans = [0]
        vowel = ['a','e','i','o','u']

        for word in words:
            if word[0] in vowel and word[-1] in vowel:
                ans.append(ans[-1]+1)
            else:
                ans.append(ans[-1])

        #now we have the total number of words that start and end with a vowel
        
        for left, right in queries:
            final.append(ans[right+1] - ans[left])
        return final




