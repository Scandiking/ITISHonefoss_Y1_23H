#This program demonstrates how a floating-point
#number can be displayed as currency. 
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print(f'Your annual pay is ${annual_pay:,.2f}')

#,.2f
#Comma (,) to indicate comma symbol as number separator. 1,000.00 instead of 1000.00.
#.2 to indicate we want two decimals.
#f as type designator (f for fixed (number of digits))
