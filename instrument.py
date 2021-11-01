instrumenten = {}

aantaL_instrumenten_invoer = input("hoeveel instrumenten wil je toevoegen?")
i = 0
j = int(aantaL_instrumenten_invoer)

while i < j:
    # dynamically create key
    key = input("Wat voor instrument")
    # calculate value
    value = input("Wat is de prijs")
    instrumenten[key] = value 
    i += 1

print(instrumenten)
print(instrumenten.get(input("Welk instrument wil je?")))