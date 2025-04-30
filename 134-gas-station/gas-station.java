class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int gasTotal = 0;
        for(int i:gas){
            gasTotal += i;
        }
        int costTotal = 0;
        for(int i:cost){
            costTotal += i;
        }
        if(costTotal > gasTotal){
            return -1;
        }
        int tank = 0;
        int start = 0;
        for(int i=0;i<gas.length;i++){
            tank = tank + gas[i] - cost[i];
            if(tank < 0){
                start = i + 1;
                tank = 0;
            }
        }
        return start;
    }
}