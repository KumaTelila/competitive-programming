class Solution {
public:
    void sortColors(vector<int>& nums) {
       int len = nums.size();
        for(int i=0; i<len; i++){
            for(int j = 0; j<len-1; j++){
                if(nums[j+1]<nums[j]){
                   swap(nums[j], nums[j+1]);
                }
            }
        }
       
    }
};