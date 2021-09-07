# custom-object.py
  
def calculateTax(taxPercent):
    return amount * taxPercent/100.0
    
def calculateTip(tipPercent):
    return amount * tipPercent/100.0
    
def calculateTotal(taxPercent, tipPercent):
    return amount * (1 * taxPercent/100.0 + tipPercent/100.0)
    
amount = 100

taxPercent = 7.5
tipPercent = 20.0

tax = calculateTax(taxPercent)
tip = calculateTip(tipPercent)

print('Tax: ', tax)
print ('Tip: ', tip)
print ('Total: ', (amount + calculateTotal(taxPercent, tipPercent))) 


