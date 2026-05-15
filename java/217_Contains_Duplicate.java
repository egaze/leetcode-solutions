// Thought Process:
// Brute force: Nested loop approach. For each element, going through to find a duplicate and returning true if found.

// Optimal: Use of a hashset. 
// Create a hashset with the array. Since they don't allow duplicates, 
// you can compare the length of the hashset with the original. 
//
// 		If shorter: duplicate
// 		else: no duplicate
								
// More optimal (Shown in solution below):
// 	Before adding element to hashSet, check if hashSet already contains element. 
// 				If it does: return true,
// 				else: add,
											
// 				out of for loop: return false

import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> duplicateSet = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (duplicateSet.contains(nums[i])) {
                return true;
            }
            duplicateSet.add(nums[i]);
        }
        return false;
    }
}