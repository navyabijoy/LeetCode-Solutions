class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        int direction = 1;
        int row = 0;
        int col =-1;
        int m = matrix.length;
        int n = matrix[0].length;

        while(m > 0 && n > 0){
            for(int i = 0; i < n;i++){
                col = col + direction;
                res.add(matrix[row][col]); 
            }
            m--;
            for(int i=0;i<m;i++){
                row = row + direction;
                res.add(matrix[row][col]);
            }
            n--;

            direction = direction * -1;
        }
        return res;
    }
}