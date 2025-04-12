#Programstart (oval)
#Less in timelønn (input)
#Les in antall arbeidstimer (input)
#beregn bruttolønn (beregning)

#Ikke glem kolon på if-betingelse.
#
#if betingelse:
#   "så-blokk" (betingelse oppfylt)
#
#else:
#   ellers-blokk (betingelse ikke oppfylt)
#
#Beregning av bruttolønn, skattetrekk og netto utbetalt
# Først trenger vi input fra brukeren.

timelonn=float(input('Hva er din timelønn? '))
antall_timer=float(input('Hvor mange timer har du jobbet? '))

#Beregner bruttolønn
bruttolonn=timelonn*antall_timer

#Finner riktig skattesats
if bruttolonn<20000:
    skattesats=28
else:
    skattesats=35

#Beregner skatt og netto lønn
skatt_i_kroner=bruttolonn*skattesats/100
nettolonn=bruttolonn-skatt_i_kroner

#Skriver ut lønnsberegningen
print('Din bruttolønn er da',format(bruttolonn,'.2f'))
print('Din skatteprosent er',skattesats,'og skattetrekket i kr er',format(skatt_i_kroner,'.2f'))
print('Du får utbetalt',format(nettolonn,'.2f'),'kr.')

