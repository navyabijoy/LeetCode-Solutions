class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if beginWord in word_set:
            word_set.remove(beginWord)

        q = deque()
        q.append((beginWord,1))
        
        while q:
            word, step = q.popleft()
            if word == endWord:
                return step

            word_char = list(word)

            for i in range(len(word)):
                org_char = word_char[i]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    word_char[i] = ch
                    new_word = "".join(word_char)
                    if new_word in word_set:
                        word_set.remove(new_word)
                        
                        q.append((new_word, step+1))
                word_char[i] = org_char 
        return 0   
