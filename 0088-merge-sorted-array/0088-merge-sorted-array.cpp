class Solution {
public:
    void merge(vector<int>& n1, int m, vector<int>& n2, int n) {
        int l = m + n -1;

        while(m > 0 && n >0){

            if(n1[m-1] > n2[n-1]){
                n1[l] = n1[m-1];
                m--;
            }else{
                n1[l] = n2[n-1];
                n-=1;
            }
            l -=1;

        }


        while( n >0){
            n1[l--] = n2[n-1];
            n--;
        }
        
    }
};