class Solution {
public:
    bool isPerfectSquare(int num) {
        int a = (int) sqrt(num);
        return a * a == num;
        
    }
};