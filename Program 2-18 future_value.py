#Get the desired future value. 
future_value = float(input('Skriv inn ønsket fremtidig verdi: '))

#Get the annual interest rate.
rate = float(input('Skriv inn årlig renterate: '))

#Get the number of years that the money will appreciate.
years = int(input('Skriv inn antall år pengene skal oppbevares: '))

#Calculate the amount needed to deposit.
present_value = future_value / (1.0 + rate)**years

#Display the amount needed to deposit
print('Du må sette inn', present_value, 'for å nå sparemålet.')

#Legg merke til antall desimaler som vises her. Se program 2-21 for å angi antall desimaler.
