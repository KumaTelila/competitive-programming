class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string>v2;
        for(int i=1; i<=n; i++){
            if(i%3==0 && i%5 == 0){
                v2.push_back("FizzBuzz");
            }else if(i%3==0){
                v2.push_back("Fizz");
            }else if(i%5==0){
                v2.push_back("Buzz");
            }else{
                string s = to_string(i);
                v2.push_back(s);
            }
        }
        return v2;
    }
};