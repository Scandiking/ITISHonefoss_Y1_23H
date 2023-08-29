#This progam demonstrates how a floating-point
#number can be rounded.
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f'The monthly payment is {monthly_payment: .2f}.')

#.2 is a precision designator that indicated the number should be rounded to two decimal places.
#f is a type designator and indicates which calue should be displayed with a fixed number of digits after the decimal point.
