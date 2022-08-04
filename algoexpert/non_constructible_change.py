#given array of positive integers representing 
#coin values, return minimum amount of change
#that can't be created
#ex: given coins=[1,2,5] min amount of change 
# can't be created is 4
def nonConstructibleChange(coins):
	#sort the coin values in ascending order
    coins.sort()
    min_coin_value = 0
    #while iterating through list check if the coin value 
    # is below the sum of previous coins of lower denomination
    # if, yes, sum_of_coins+1 is the min change that can't be created
    # if not continue till the end of list and return sum_of_coins+1
    for coin in coins:
      if coin > min_coin_value + 1:
        return min_coin_value+1
      min_coin_value+=coin
    return min_coin_value+1