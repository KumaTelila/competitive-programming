class Solution {
public:
    string reverseParentheses(string s) {
         stack<int>st;
         string a = "";
        int l = s.length();
        for(int i=0; i<l; i++){
           if(s[i]=='('){
               st.push(i);
           }
           else if(!st.empty() && s[i]==')'){
               reverse(s.begin()+st.top(), s.begin()+i);
               cout<<st.top()<<endl;
               cout<<i<<endl;
               cout<<s;
               st.pop();

           }
        }
        for(int i=0; i<l; i++){
            if(s[i]=='(' || s[i]==')'){
                continue;
            }else{
                a.push_back(s[i]);
            }
        }
        return a;
        
    }
};