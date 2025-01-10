#include<cctype>
class Solution {
public:
    bool isPalindrome(string s) {
        
        int l = 0;
        int r = s.size();

        while(l < r){

            while(l < r && !isalnum(s[l])){
                l++;
            }
            while(l < r && !isalnum(s[r])){
                r--;
            }

            if(std::tolower(s[l]) != std::tolower(s[r])){
                return false;
            }
            l++;
            r--;
        }

        return true;
    }
};