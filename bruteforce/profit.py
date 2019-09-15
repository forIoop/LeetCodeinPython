
def profit(info):
	if info["sell_price"] > info["cost_price"]:
		unit_profit = info["sell_price"] - info["cost_price"]
	
	else:
		unit_profit = info["cost_price"] - info["sell_price"]
		
	return round(unit_profit * info["inventory"])
