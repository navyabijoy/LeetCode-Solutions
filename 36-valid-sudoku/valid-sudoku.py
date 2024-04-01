class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(input_list):
            seen = set() #if just written as () then a tuple is created
            for num in input_list: #iterate through the numbers encountered
                if num != ".": #if the box is not blank
                    if num in seen: #but if the num encountered is already in the hash set
                        return False #return false
                seen.add(num) #if the number is not repeated, the add it to the hash set
            return True #return true in the end

        for i in range(9): #to iterate through each row
            if not is_valid(board[i]) or not is_valid([board[j][i]  for j in range(9)]):
                return False #since the duplicate is found return false
        

        #for row in board:
         #   if not is_valid(row):
              #  return False

        #for col in zip(*board):
            #if not is_valid(col):
                #return False
        
        for i in range (0,9,3): #iterate through the numbers, start from 0, till 9 and increament by 3
            for j in range (0,9,3): #same for the columns, this is to identify the boxes
                sub_box = [board[x][y] for x in range (i,i+3)for y in range (j,j+3)] #create a list of the sub boxes to find duplicate
                if not is_valid(sub_box): #if a duplicate is found in teh boxes the return false
                    return False
        return True