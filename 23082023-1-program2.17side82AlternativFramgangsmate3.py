#Program 2-17 side 82, alternativ framgangsmåte 3
#Gjøre om fra sekunder til timer, minutter og sekunder

#Ber brukeren om oppgi antall sekunder
antall_sekunder=int(input('Oppgi antall sekunder som skal konverteres: '))

#Beregner antall timer
antall_timer=antall_sekunder//3600
resterende_sekunder_etter_timer=antall_sekunder%3600

#Beregner antall gjenværende minutter og sekunder
antall_minutter=resterende_sekunder_etter_timer//60
resterende_sekunder_etter_minutter=resterende_sekunder_etter_timer%60

#Utskrift av resultat
print(antall_sekunder,'sekunder gjort om til timer, minutter og sekunder blir: ')
print('Timer:',antall_timer)
print('Minutter:',antall_minutter)
print('Sekunder:',resterende_sekunder_etter_minutter)
