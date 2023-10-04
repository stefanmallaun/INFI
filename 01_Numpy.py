import numpy as np

a = np.array([1, 2, 3, 4, 5])

#1.1.1
b = np.arange(100, 201)

#1.1.2
b = np.arange(100, 201, 2)

#1.1.3
c = np.arange(100, 111, 0.5)

#1.1.4
#Normalverteilung
d = np.random.normal(0, 100, 100)


#Einfache Berechnung 
#Mittelwert
e = np.mean(d)
#Median
f = np.median(d)
#Minimum
g = np.min(d)
#Maximum
h = np.max(d)
#Standard deviation
i = np.std(d)
#In welchem Bereich liegen die mittleren 95%? Welche Werte sind das die außerhalb liegen?
j = np.percentile(d, 95)
#Alle Zahlen mit 100 mulitplieren
k = d*100
#Nur die ersten 10 Zahlen auswählen
l = d[:10]
#Nur die Zahlen auswählen, die größer 0 sind
m = d[d>0]


print(a, b, c, d, e, f, g, h, i, j, k)