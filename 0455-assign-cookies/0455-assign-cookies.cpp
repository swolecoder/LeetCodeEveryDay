class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {

        int i =0;
        int count =0;
        std::sort(g.begin(), g.end());
        std::sort(s.begin(),s.end());
          // for (int j = 0; j < s.size() && i < g.size(); j++) {
        for(int j =0; j < s.size() && i < g.size();j++){
            if(s[j] >=  g[i]){
                count++;
                i++;
            }
        }
        return i;
        
    }
};