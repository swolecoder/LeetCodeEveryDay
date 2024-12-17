class Solution {
public:
    bool checker(string& s){
        int left = 0;
        int right = s.length()-1;
        while(left <right){
            if(s[left] != s[right]){
                return false;

            }
            left +=1;
            right -=1;
        }
        return true;
    }
    string firstPalindrome(vector<string>& words) {

        for(auto& word: words){
            if(checker(word)){
                return word;
            }
        }
        return "";
        
    }
};