def maxProfit(stocks):
    max_profit=0 #Holder for purchase price
    cur_profit=0
    b_price=-1 #The stock price you are buying
    s_price=-1 #The stock price you are selling
    change_b = True
    
    for i in range(0, len(stocks)-1):
    	s_price = stocks[i+1]
        
        if (change_b):
        	b_price = stocks[i]

        if (s_price < b_price):
        	change_b = True

    	else: 
    		cur_profit = s_price - b_price
    		if cur_profit > max_profit:
    			max_profit=cur_profit
    			change_b = False
    return max_profit

stockList = [30, 33, 33, 15, 16]
print (maxProfit(stockList))




    

    