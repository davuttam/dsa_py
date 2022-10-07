# Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
# Output: 3 (1-> 3 -> 9 -> 9)
# Explanation: Jump from 1st element 
# to 2nd element as there is only 1 step, 
# now there are three options 5, 8 or 9. 
# If 8 or 9 is chosen then the end node 9 
# can be reached. So 3 jumps are made.

# Input:  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
# Output: 10
# Explanation: In every step a jump 
# is needed so the count of jumps is 10.
# https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
# TODO:

# Greedy approach
def minJump(nums):
    jumps = 0
    current_jump_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_jump_end:
            jumps += 1
            current_jump_end = farthest
    return jumps