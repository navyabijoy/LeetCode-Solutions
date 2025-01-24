class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        answer.append([1]) # by default
        for i in range(numRows - 1):
            newRow = [1]
            for j in range(i):
                newRow.append(answer[i][j] + answer[i][j+1])
            newRow.append(1) # ending each row with 1
            answer.append(newRow)
        return answer