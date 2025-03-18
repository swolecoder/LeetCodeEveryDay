class Solution {
public:
    int calPoints(vector<string>& o) {
        vector<int> ans;

        for(int i =0; i < o.size(); i++){
            if(o[i] == "+"){
                int top= ans.back();
                int b = ans[ans.size() -2];
                int d = top + b;
                ans.push_back(d);
            }else if(o[i] == "D" ){
                int top = ans.back();
                ans.push_back(2 * top);
            }else if(o[i] == "C"){
                ans.pop_back();
            }else{
                ans.push_back(stoi(o[i]));
            }
        }

        int res = 0;
        for(int i =0; i < ans.size(); i++){
            res += ans[i];        
         }
        return res;
        
    }
};