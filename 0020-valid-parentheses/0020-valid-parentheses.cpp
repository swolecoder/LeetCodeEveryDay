class Solution {
public:
    bool isValid(string s) {
        std::stack<char> st;
         std::unordered_map<char, char> map = {
            {'(',')'},
            {'[',']'},
            {'{','}'}
        };

        for(auto ch: s){
            if(map.count(ch)){
                st.push(ch);
            }else{

                if(!st.empty() && map[st.top()] == ch){
                   st.pop();
                }else{
                   return false;
                }
            }
        }

        return st.empty();
        
    }
};