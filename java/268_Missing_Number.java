// Brute force: check entire array for each number in the range

// Optimal: 
// - Perform a sum of comsecutive numbers to n ( i.e. n(n+1)/2 )
// - Perform a sum of the numbers in nums
// - Subtract the two sums to get the missing element								

class Solution {
    public int missingNumber(int[] nums) {
        int sum = 0;
        int n = nums.length;
        int consecutiveSum = (n * (n + 1))/2;
        System.out.println(consecutiveSum);

        for (int i = 0; i < n; i++) {
            sum += nums[i];
        }
        System.out.println(sum);

        return consecutiveSum - sum;
    }
}