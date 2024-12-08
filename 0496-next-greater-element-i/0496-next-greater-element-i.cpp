#include <vector>
#include <unordered_map>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> map;
        stack<int> s;

        // Step 1: Find the next greater element for each element in nums2
        for (int i = nums2.size() - 1; i >= 0; i--) {
            while (!s.empty() && nums2[i] >= s.top()) {
                s.pop();
            }

            map[nums2[i]] = s.empty() ? -1 : s.top();
            s.push(nums2[i]);
        }

        // Step 2: Create the result for nums1 using the map
        vector<int> ans(nums1.size());
        for (int i = 0; i < nums1.size(); i++) {
            ans[i] = map[nums1[i]];
        }

        return ans;
    }
};
