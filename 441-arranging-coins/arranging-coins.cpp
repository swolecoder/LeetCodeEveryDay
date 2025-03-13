class Solution {
public:
    int arrangeCoins(int n) {

        int l = 0;
        int r = n;
        long res = 0;

        while(l <=r){
            long mid = (l+r)/2;
            long coin = (( mid) * (mid+1)/2);

            if(coin > n){
                r = mid -1;
            }else{
                res = max(res, mid);
                l = mid +1;
            }
        }

        return res;
    }
};