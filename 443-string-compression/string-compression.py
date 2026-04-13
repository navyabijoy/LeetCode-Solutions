class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        index = 0

        while i < n:
            curr_char = chars[i]
            count = 0

            # count the curr character
            while i < n and curr_char == chars[i]:
                count += 1
                i += 1

            # now we have the alphabet and the count, assign it
            chars[index] = curr_char
            index += 1
            if count > 1:  # should be present only if value greater than 1
                str_count = str(count)
                for c in range(len(str_count)):
                    chars[index] = str_count[c]
                    index += 1

        return index
