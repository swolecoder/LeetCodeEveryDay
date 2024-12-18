#include <vector>
#include <algorithm>
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int l=0;
        int r = nums.size()-1;

        while(l < r){
            if(nums[l] % 2 ==0){
                l +=1;
            }
            else if(nums[r] % 2 == 1){
                r -=1;
            }else{
                std::swap(nums[l], nums[r]);
                l +=1;
                r -=1;
            }

           
        } 
        return nums;
        
    }
};