#Doug Westbrook
#P2HW2 Tip, Tax, and Total
#021518




foodCost= float(input ("What is the cost of the meal?\t",  ))

tipAmount = foodCost * .18
taxAmount = foodCost * .07

mealCost = foodCost + tipAmount + taxAmount

print ("Food Cost is\t", "$", format (foodCost,".2f"))
print ("Tip is\t\t", "$ ", format(tipAmount,'.2f'))
print ("Tax is\t\t", "$ ", format (taxAmount,".2f"))
print ("Total meal Cost\t", "$", format (mealCost,".2f"))
       

