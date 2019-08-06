#Find how many days are in each month
from calendar import monthrange
def day_amount(month, year):
	month_range = monthrange(year,month)
	return month_range[1]
