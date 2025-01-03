#include<algorithm>
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }

        // std::sort(s.begin(), s.end());
        // std::sort(t.begin(), t.end());
        // return s == t;

        std::unordered_map<char, int> dict;

        for(auto& ch:s){
            dict[ch]++;
        }


        for(auto& ch: t){
            if(dict.find(ch) == dict.end()){
                return false;
            }
            dict[ch] -=1;
            if(dict[ch] == 0){
                 dict.erase(ch);

            }

        }

        return dict.empty();
        
    }
};