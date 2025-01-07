class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string,vector<string>> map;

        for(auto str:strs){
           string data = str;
           std::sort(data.begin(), data.end());
           map[data].push_back(str);
        }

        vector<vector<string>> res;
        for(auto[k,v]: map){
            res.push_back(v);
        }
        return res;
    }
};