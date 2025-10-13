class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if beginWord in word_set:
            word_set.remove(beginWord)

        q = deque()
        q.append((beginWord,1))

        while q:
            word, steps = q.popleft()
            # found the target
            if word == endWord:
                return steps
            
            # Try changing each character
            for i in range(len(word)):
                org_char = word[i] # the word we will be changing to other characters
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    word = word[:i] + ch + word[i+1:]
                    if word in word_set:
                        word_set.remove(word)
                        q.append((word,steps+1))
                word = word[:i] + org_char + word[i+1:]

        # no transformation possible
        return 0


