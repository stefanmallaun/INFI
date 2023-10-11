import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('INFI\data\london_weather.csv', delimiter=",", skip_header=1)

dates = data[:, 0]
years = np.floor(dates / 10000).astype(int)

average_temperature = np.mean(data[:, 2])
print("Average Temperature:", average_temperature)

# Task 2: Temperatur Unterschied darstellen

selected_years = [1979, 1989, 1999, 2009]
selected_data = [data[years == year][:, 2] for year in selected_years]

plt.figure()
plt.boxplot(selected_data)
plt.xticks(range(1, len(selected_years) + 1), selected_years)
plt.title("Temperature Differences Over the Years")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.show()

# Task 3: Zeitlicher Verlauf 

specific_year = 2000
yearly_data = data[years == specific_year]
days = np.arange(1, len(yearly_data) + 1)
temperature = yearly_data[:, 2]

plt.figure()
plt.plot(days, temperature, marker='o', linestyle='-')
plt.title(f"Temperature Curve for {specific_year}")
plt.xlabel("Day of the Year")
plt.ylabel("Temperature (°C)")
plt.show()

# Task 4: Wetterextremen
specific_year = 2000
yearly_data = data[years == specific_year]
temperature_data = yearly_data[:, 2] 


q1 = np.percentile(temperature_data, 25)
q3 = np.percentile(temperature_data, 75)
iqr = q3 - q1


outlier_threshold = 1.5 * iqr


extreme_values = temperature_data[(temperature_data < q1 - outlier_threshold) | (temperature_data > q3 + outlier_threshold)]



plt.figure()
plt.boxplot(temperature_data)
plt.title(f"Temperature Distribution for {specific_year} with Extreme Values Highlighted")
plt.ylabel("Temperature (°C)")

# Task 5: Bar Chart
last_10_years = np.unique(years)[-10:]
average_temperatures_last_10_years = [np.mean(data[years == year][:, 2]) for year in last_10_years]

plt.figure()
plt.bar(last_10_years, average_temperatures_last_10_years)
plt.title("Average Temperatures for the Last 10 Years")
plt.xlabel("Year")
plt.legend()
plt.ylabel("Average Temperature (°C)")
plt.show()