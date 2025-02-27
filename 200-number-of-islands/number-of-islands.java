class Pair{
    int first;
    int second;
    public Pair(int first, int second){
        this.first = first;
        this.second = second;
    }
}
class Solution {
    private void bfs(int ro, int co,int [][] vis,char[][] grid){
        int m = grid.length;
        int n = grid[0].length;

        vis[ro][co] = 1;
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(ro,co));

        int[] delRow = {-1,1,0,0};
        int[] delCol = {0,0,-1,1};
        while(!q.isEmpty()){
            Pair p = q.poll();
            int row = p.first;
            int col = p.second;
            
            for(int i = 0;i<4;i++){
                    int nrow = row + delRow[i];
                    int ncol = col + delCol[i];
                    if(nrow>=0 && nrow < m && ncol >= 0 && ncol < n 
                    && grid[nrow][ncol] == '1' && vis[nrow][ncol] == 0){
                        vis[nrow][ncol] = 1;
                        q.add(new Pair(nrow, ncol));
                    }
                }
            
        }
    }
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int [][] vis = new int[m][n];
        int cnt = 0;
        for(int row = 0; row < m; row++){
            for(int col = 0; col < n; col++){
                if(vis[row][col] == 0 && grid[row][col] == '1'){
                    cnt++;
                    bfs(row,col,vis,grid);
                }
            }
        }
        return cnt;
    }
}