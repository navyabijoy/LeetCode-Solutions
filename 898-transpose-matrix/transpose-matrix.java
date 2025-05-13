class Solution {
    public int[][] transpose(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] mat = new int[n][m];
        for(int r = 0; r < m; r++){
            for(int c = 0; c < n; c++){
                int temp = matrix[r][c];
                mat[c][r] = temp;
            }
        }
        return mat;
    }
}