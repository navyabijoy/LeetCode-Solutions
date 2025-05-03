class Solution {
    private boolean dfs(int row, int col, char[][] grid, int index, String word){
        if(word.length() == index){
            return true; // the entire word has been traversed
        }
        if( row < 0 || row >= grid.length ||  col < 0 || col >= grid[0].length || grid[row][col] != word.charAt(index)){
            return false;
        }
        char temp = grid[row][col]; // store the original value in temp as we have to backtrack
        grid[row][col] = 'v'; // mark visited

        int[][] direction = {{0,1},{0,-1},{1,0},{-1,0}};
        for(int[] dir:direction){
            int newRow = row + dir[0];
            int newCol = col + dir[1];
            if(dfs(newRow, newCol, grid, index+1,word)){
                return true;
            }
        }
        grid[row][col] = temp; // backtrack, set it back to its previous value
        return false;
    }
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        for(int r = 0; r < m; r++){
            for(int c = 0; c < n; c++){
                if(dfs(r,c,board,0,word)){
                    return true;
                }
            }
        }
        return false;
    }

}