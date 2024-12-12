class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i=0;
        int j = 0;
        string ans;

        while(i < word1.size() && j < word2.size()){
           // cout<< "Ashish";
           cout<<word1[i]<<endl;
            ans.push_back(word1[i]);
            ans.push_back(word2[j]);
            i +=1;
            j +=1;
        }
        cout<<ans;
        while( i < word1.size()){
            ans.push_back(word1[i]);
            i+=1;
        }


        while(j < word2.size()){
           ans.push_back(word2[j]);
            j+=1;
        }
        cout << ans;
        return ans;
        
    }
};