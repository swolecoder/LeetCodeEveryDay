class Solution {
    func minimumDifference(_ nums: [Int], _ k: Int) -> Int {

       var ans = Int.max
       var num = nums.sorted()
       var l = 0
       var r = k-1

       while r < nums.count {
        ans = min(ans, num[r]-num[l])
        l+=1
        r+=1
       }

       return ans

        
    }
}