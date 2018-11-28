#Pseudo Code
# Iterate through all of the stock values within the provided list
# Compare the ith index(buying) price and i+1 selling index price
# If the selling price is larger, i is the buying index and i+1 is the selling index
# 	Calcualte the current profit and check if it is a new maximum profit; restart this loop from step 2
# Otherwise, the buying price is greater so keep the buy price the same and change the set price
# 
def maxProfit(stocks):
    max_profit=-1 #Holds the maximum profit one can make while searching
    cur_profit=0 #Temporary holder for the profit while searching
    b_price=-1 #The stock price you are buying
    s_price=-1 #The stock price you are selling
    change_b = True #Flag to determine if iteration should move to new buying price
    
    for i in range(0, len(stocks)-1):

    	#Iterate the selling price to be the next price in the index
    	s_price = stocks[i+1]
        
        #If this flag is true, we must set the buying price to the current index
        if (change_b):
        	b_price = stocks[i]

        #If the buying price is greater than the selling price, set the change flag to true to set a new buying price
        if (s_price < b_price):
        	change_b = True
        	continue
        #Otherwise the selling price is higher, so see if it is a new maximum and keep the buying price the same
    	else: 
    		cur_profit = s_price - b_price
    		if cur_profit > max_profit:
    			max_profit=cur_profit
    			change_b = False
    return max_profit

#Testing the Function
stockList = [30, 33, 60, 15, 16, 17]
print (maxProfit(stockList))




    

    