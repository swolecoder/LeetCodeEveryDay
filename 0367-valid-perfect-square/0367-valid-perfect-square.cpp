class Solution {
public:
    bool isPerfectSquare(int num) {
        // int a = (int) sqrt(num);
        // for(long long i=1; i <= a; i++){
        //     long long d = i * i;
        //     if(d > num){
        //         return false;
        //     }
        //     if(d == num){
        //         return true;
        //     }
        // }
        // return false;
        long l = 0;
        long long r = num;

        while(l <= r){
            long long mid =  l + (r-l)/2;
            if( mid* mid > num){
                r = mid-1;
            }else if(mid * mid < num){
                l = mid +1;
            }else{
                return true;
            }
        }
        return false;
        
    }
};