Algorithm:
1. take the first value from the prices as min_price
2. take the profit variable as 0 at first
3. loop thru the list
4. if price < min_price update the min_price with current price
5. else find the diff = prices[price] - min_price
6. sum up the profit and update the min_price wth current price
7. return profit