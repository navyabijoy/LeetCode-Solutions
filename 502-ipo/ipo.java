class Solution {
    class Pair{
        int profit;
        int capital;
        Pair(int profit, int capital){
            this.profit = profit;
            this.capital = capital;
        }
    }
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        PriorityQueue<Pair> minHeap = new PriorityQueue<>(new Comparator<Pair>(){
            public int compare(Pair p1, Pair p2){
                return Integer.compare(p1.capital, p2.capital);
            }
        });
        PriorityQueue<Pair> maxHeap = new PriorityQueue<>(new Comparator<Pair>(){
            public int compare(Pair p1, Pair p2){
                return Integer.compare(p2.profit, p1.profit);
            }
        });

        for(int i=0;i<profits.length;i++){
            minHeap.add(new Pair(profits[i], capital[i]));
        }

        while(k>0){
            while(!minHeap.isEmpty() && minHeap.peek().capital<=w){
                maxHeap.add(minHeap.remove());
            }
            if(maxHeap.isEmpty()) break;
            w += maxHeap.remove().profit;
            k--;
        }
        return w;
    }
}