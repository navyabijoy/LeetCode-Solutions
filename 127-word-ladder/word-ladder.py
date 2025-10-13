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

            word_chars = list(word)  
            # Try changing each character
            for i in range(len(word)):
                org_char = word_chars[i] # the word we will be changing to other characters
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    word_chars[i] = ch
                    next_word=  "".join(word_chars)
                    if next_word in word_set:
                        word_set.remove(next_word)
                        q.append((next_word,steps+1))
                word_chars[i] = org_char

        # no transformation possible
        return 0


