class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        left = 0
        n =  len(words)
        vowels = {'a','e','i','o','u'}
        prefix_sum = [0] * (n+1)
        
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix_sum[i+1] = 1

        for i in range(1,n+1):
            prefix_sum[i] += prefix_sum[i-1]

        ans = []
        for l1, r1 in queries:
            ans.append(prefix_sum[r1+1] - prefix_sum[l1]) 

        
        return ans
        # final = []
        # ans = []
        # PreCount = 1
        # i = 0

        # for word in words:
        #     if word[0] in vowels and word[len(word)-1] in vowels:
        #         PreCount += 1
        #     ans.append(PreCount)
        # #now we have the total number of words that start and end with a vowel
        
        # while i < len(queries):
        #     left = queries[i][0]
        #     right = queries[i][1]
        #     final.append(sum(ans[left:right]))
        #     i += 1
        # return final




