class Solution {
    public boolean isAnagram(String s, String t) {
        
        HashMap<Character, Integer> s1 = new HashMap<>();
        HashMap<Character, Integer> t1 = new HashMap<>();
        int slen = s.length();
        int tlen = t.length();
        if(slen != tlen){
            return false;
        }
        for(int i = 0; i < slen; i++){
            s1.put(s.charAt(i), s1.getOrDefault(s.charAt(i),0)+1);
        }
        for(int i = 0; i < tlen; i++){
            t1.put(t.charAt(i), t1.getOrDefault(t.charAt(i),0)+1);
        }
        if(s1.equals(t1)){
            return true;
        }
        return false;
    }
}
