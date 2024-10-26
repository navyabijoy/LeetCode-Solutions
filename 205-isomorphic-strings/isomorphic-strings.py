class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_to_t = {}
    
        for char_s, char_t in zip(s, t):
            # Check if the current char_s is already mapped
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                # Ensure char_t is not already mapped to another char_s
                if char_t in map_s_to_t.values():
                    return False
                map_s_to_t[char_s] = char_t
        
        return True
        