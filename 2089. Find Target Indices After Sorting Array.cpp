class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        int len = nums.size();
        vector<int>n;
        sort(nums.begin(), nums.end());
        for(int i=0; i<len; i++){
            if(nums[i]==target){
                n.push_back(i);
            }
        }
        return n;
    }
};