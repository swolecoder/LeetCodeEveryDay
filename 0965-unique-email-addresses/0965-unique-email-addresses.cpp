class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        std::unordered_set<string> seen;
        string local;
        string domain;

        for(auto& email: emails){
            int pos = email.find("@");
            local = email.substr(0, pos);
            domain = email.substr(pos+1);

            string find;
            bool ignore = false;
            for(auto& ch : local){

                if(ch == '+'){
                ignore = true;
                break;
                }else if(!ignore && ch != '.'){
                    find += ch;
                }
            }

            string found = find + "@" + domain;
            seen.insert(found);
            
            
        }





        return seen.size();

        
    }
};