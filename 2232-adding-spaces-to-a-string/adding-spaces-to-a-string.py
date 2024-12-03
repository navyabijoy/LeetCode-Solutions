class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        final = []
        space_index = 0
        num_spaces = len(spaces)
        for i, char in enumerate(s):
            if space_index < num_spaces and i == spaces[space_index]:
                final.append(' ')
                space_index += 1
            final.append(char)
        return ''.join(final)

