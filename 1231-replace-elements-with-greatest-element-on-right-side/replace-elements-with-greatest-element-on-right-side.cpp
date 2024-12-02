class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int n = arr.size();
        std::vector<int> ans(n,-1);
        int max_found =-1;

        for(int i= arr.size()-1; i >=0; i--){
            ans[i] = max_found;
            max_found = std::max(max_found,arr[i]);

        }
        return ans;
        
    }
};