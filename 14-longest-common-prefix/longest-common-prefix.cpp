class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {

        if(strs.empty()){
            return "";
        }
        int min_length = strs[0].length();
        string ans= "";

        //find the minlengfth
        for(auto& str: strs){
            min_length = std::min(min_length, (int)str.length());
        }
        cout <<min_length<<endl;

        for(int i =0; i < min_length; i++){
            char match = strs[0][i];
            bool check = true;

            for(auto& str: strs){
                if(match != str[i]){
                    check = false;
                    break;
                }
            }
            if(check){
                ans += match;
            }else{
                break;
            }
        }




        return ans;
        
    }
};