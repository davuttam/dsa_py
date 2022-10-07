import math

# TODO:



def coin_change(coins, amts):
    ans = math.inf
    if amts == 0: return 0 
    for cn in coins:
        if amts-cn >= 0:
            sub_ans = subcoin_change(coins, amts-cn)

            if sub_ans != math.inf:
                ans += 1
    return ans
























class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        sml_cnt = math.inf
        # fnl_memo = {}
        def final_coin_change(coins, amt, cur_cnt=0):
            nonlocal sml_cnt
            if amt == 0:
                if sml_cnt > cur_cnt:
                    sml_cnt = cur_cnt
                return 0
            for cn in coins:
                rem_amt = amt - cn
                if rem_amt >= 0:
                    final_coin_change(coins, rem_amt, cur_cnt+1)
        
        final_coin_change(coins, amount)
        return sml_cnt

def coinChange(coins, amount: int) -> int:
    if amount == 0: return 0
    
    ans = math.inf

    for i in range(len(coins)):
        if amount-coins[i] >= 0:
            sub_ans = coinChange(coins, amount-coins[i])
            if sub_ans > -1 and sub_ans + 1 < ans:
                ans = sub_ans + 1
                
    return -1 if ans == math.inf else ans