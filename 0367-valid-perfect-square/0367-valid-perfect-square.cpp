class Solution {
public:
    bool isPerfectSquare(int num) {
        int a = (int) sqrt(num);
        for(long long i=1; i <= a; i++){
            long long d = i * i;
            if(d > num){
                return false;
            }
            if(d == num){
                return true;
            }
        }
        return false;
        
    }
};