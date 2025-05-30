class Solution {
    public int countNegatives(int[][] grid) {
        int  m = grid.length;
        int  n = grid[0].length;
        int count = 0;
        for(int r = 0; r < m; r++){
            for(int c = 0; c < n; c++){
                if(grid[r][c] < 0){
                    // if one element is encountered to be -ve, rest are also -ve
                    count += grid[r].length - c; 
                    break;
                }
            }
        }
        return count;
    }
}