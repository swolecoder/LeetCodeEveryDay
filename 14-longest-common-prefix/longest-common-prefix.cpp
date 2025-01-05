class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 0){
            return "";
        }

        int min = strs[0].size();

        for(auto& str: strs){
            min = std::min(min,(int)str.size());
        }
        string res = "";

        for(int i =0; i < min; i++){
            bool match = true;
            char check = strs[0][i];

            for(auto str: strs){
                if(str[i] != check){
                    match = false;
                    break;
                }
            }

            if(match){
                    res += check;
            }else{
                    break;
            }
        }
        return res;
        
    }
};