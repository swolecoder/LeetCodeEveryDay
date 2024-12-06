class Solution {
public:
    bool isIsomorphic(string s, string t) {
        std::unordered_map<char,char> s_map,t_map;

        if(s.length() != t.length()){
            return false;
        }

        for(int i =0; i < s.length(); i++){
             if(s_map.find(s[i]) != s_map.end()){
                if(s_map[s[i]] != t[i]){
                    return false;
                }
             }else{
                s_map[s[i]] = t[i];
             }
             if(t_map.find(t[i])  != t_map.end()){
                if(t_map[t[i]] != s[i]){
                    return false;
                }
                
             }else{

                t_map[t[i]] = s[i];
             }

        }
        return true;
       
    }
     
};