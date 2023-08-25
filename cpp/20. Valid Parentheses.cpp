class Solution {
public:
    bool isValid(string s) {
        stack<char>st;
        int l = s.length();
        for(int i = 0; i<l; i++){
            if(st.empty()){
                st.push(s[i]);
            }else if((st.top() == '(' && s[i] == ')')
                 || (st.top() == '{' && s[i] == '}')
                 || (st.top() == '[' && s[i] == ']')){
                     st.pop();
                 }else{
                     st.push(s[i]);
                 }
        }
         if (st.empty()) {
         
        return true;
    }
    return false;
        
    }
};