class Solution {
    private int checkDrop(int m, int n, int i, int[][] grid){
        int row = 0;
        int col = i;
        while(row<m) {
            int next_col = col + grid[row][col];

            if(next_col < 0 || next_col > n-1 || grid[row][col] != grid[row][next_col])
            {
                return -1;
            }
            row++;
            col = next_col;
        }
        return col;

    }

    public int[] findBall(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] res = new int[n];
        
        for(int i = 0; i < n; i++){
            res[i] = checkDrop(m,n,i,grid);
        }
        return res;
    }
}