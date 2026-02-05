daily_sales = [2,35,565,123,343,1,64,7,34]

total_cups = sum( sale for sale in daily_sales if sale > 64)
print(total_cups)