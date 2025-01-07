class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, vector<string>> map;

        for(auto str: strs){
            vector<int> data(26,0);
            for(int i =0; i < str.size(); i++){
                data[str[i] -'a']++;
            }

            string key;

            for(int i = 0; i < 26; i++){
                key += "#" + to_string(data[i]);
            }

            map[key].push_back(str);
        }      

        vector<vector<string>> ans;

        for(auto [k,v]: map){
            ans.push_back(v);
        }

        return ans;
    }
};