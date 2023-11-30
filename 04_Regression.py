import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Lade die Daten und trainiere das Modell
population_data = pd.read_excel("data/bev_meld.xlsx")
X = population_data[['year']]
y = population_data['population']
model = LinearRegression().fit(X, y)

# Berechne die Prognose und füge sie der Tabelle hinzu
predictions = pd.DataFrame({'year': range(1980, 2031)})
predictions['predicted_population'] = model.predict(predictions)

# Verbinde die Daten und trainierte Werte
data = pd.concat([population_data, predictions], ignore_index=True)

# Plotte die Daten
plt.figure(figsize=(12, 6))
plt.plot(data['year'], data['predicted_population'], color='red')
plt.scatter(data['year'], data['population'])
plt.xlabel('Jahr')
plt.ylabel('Bevölkerung')
plt.title('Gesamtbevölkerung Tirol')
plt.show()