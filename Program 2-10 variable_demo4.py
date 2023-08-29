#Program 2-10, variable_demo4.py
#This program demonstrates variable reassignment.
#Assign a value to the dollars variable.
dollars = 2.75                                #The variable 'dollars' are now worth 2.75
print('I have', dollars, 'in my account.')    #This will output "I have 2.75 in my account."

#Reassign dollars so it references
#a different value.
dollars = 99.95
print('But now I have', dollars, 'in my account!')    #This is because 99.95 is the last assigned value to the dollars variable, and the 2.75 value is "thrown away".
