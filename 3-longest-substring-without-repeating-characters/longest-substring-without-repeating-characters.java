import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> seen = new HashSet<>();
        int left = 0, maxLen = 0;
        for(int right = 0;right < s.length();right++){
            while(seen.contains(s.charAt(right))){
                seen.remove(s.charAt(left));
                left++;
            }
            seen.add(s.charAt(right));
            maxLen = Math.max(right-left+1, maxLen);
        }
        return maxLen;
    }
}