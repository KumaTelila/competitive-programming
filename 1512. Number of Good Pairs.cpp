class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int leng = nums.size();
        int f =0;
        for(int i=0; i<leng-1; i++){
            for(int j=i+1; j<leng; j++){
                if(nums[i]==nums[j]){
                    f++;
                }
            }
        }
        return f;
    }
};