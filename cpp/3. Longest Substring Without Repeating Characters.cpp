class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length(); 
    set<char> st; 
    int longest = 0; 
  
    for (int i = 0; i < n; i++) 
    { 
        for (int j = i; j < n; j++) 
        { 
            if (st.find(s[j]) == st.end()) 
            { 
                st.insert(s[j]); 
            } 
            else
            { 
                int len = st.size(); 
                if (longest < len) 
                    longest = len; 
                st.clear(); 
                break; 
            } 
        } 
    } 
  
    int len = st.size(); 
    if (longest < len) 
        longest = len; 
  
    return longest; 
    }
};