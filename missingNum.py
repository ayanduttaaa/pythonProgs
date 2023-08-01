# Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

# Example 1:

# Input:
# N = 5
# A[] = {1,2,3,5}
# Output: 4
# Example 2:

# Input:
# N = 10
# A[] = {6,1,2,8,3,4,7,10,5}
# Output: 9

# Your Task :
# You don't need to read input or print anything. Complete the function MissingNumber() that takes array and N as input  parameters and returns the value of the missing number.


# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)


# Constraints:
# 1 ≤ N ≤ 106
# 1 ≤ A[i] ≤ 106



-------------------------------------------------------------------------------------------------------------------

class Solution:
    def missingNumber(self,array,n):
        # code here
        ns = n*(n+1)//2
        return ns-sum(array)

-------------------------------------------------------------------------------------------------------------------

# We can solve this problem by using the formula for the sum of the first N natural numbers, which is N*(N+1)/2. This gives us the total sum we should have if no number is missing. We then subtract the sum of the elements in the array from this total, which will give us the missing number.
