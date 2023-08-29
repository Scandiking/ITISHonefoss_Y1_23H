#Get a number of seconds from the user.
total_seconds = float(input('Enter a number of seconds: '))    #Gets number of secs from user, converts to a float and assigns input value to total_seconds variable

#Get the number of hours.
hours = total_seconds // 3600                                  #Calculates number of hours in input number of seconds. Integer divisioned on 3600 cuz there's so many seconds in an hour. // because no of hours w/o fractional part

#Get the number of remaining minutes.
minutes = (total_seconds // 60) % 60                           #// to divide variable total_seconds by 60 to get total no of minutes. % operator to divide total number by 60 and get remainder of division. The result is the number of the remaining minutes.

#Get the number of remaining seconds.
seconds = total_seconds % 60                                   #Calculates remaining seconds. 1 minute = 60 sec, so use % operator to divide variable total_seconds by 60 and get remainder. The result is the number of remaining seconds.

#Display the results. 
print('Here is the time in hours, minutes, and seconds:')     #Displays string of text
print('Hours:', hours)                                        #Displays calculated amount of seconds into full hours, not including remaining minutes and seconds
print('Minutes:', minutes)                                    #Displays calculated amount of seconds into full minutes, not including remaining seconds
print('Seconds:', seconds)                                    #Displays calculated amount of seconds into remaining seconds not expressed by hours and minutes
