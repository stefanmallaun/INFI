from math import nan
import numpy as np
import matplotlib.pyplot as plt
#Mallaun
d = np.genfromtxt('data\london_weather.csv', delimiter=",", skip_header=1 )

dt =  d[:,0] #Datum mit folgendem Aufbau: 19790103 (3.Jänner 1979)
# Aufteilen in Tag, Monat, Jahr
day = (dt % 100).astype('i')
month = (dt % 10000 / 100).astype('i')
year = (dt % 100000000 / 10000).astype('i')

# Check ob es funktioniert hat
print("Jahr:", np.unique(year, return_counts=True))
print("Monat", np.unique(month, return_counts=True))
print("Tag:", np.unique(day, return_counts=True))
print("Jahr MIN MAX" , np.min(year), np.max(year))

sun = d[:,2] # Sonnenstunden

max_temp = d[:,4]

mean_temp = d[:,5] 

min_temp=d[:,6]

radiation = d[:,3]

mean_temp_1979 = mean_temp[year == 1979]

mean_temp_1989 = mean_temp[year == 1989]

mean_temp_1999 = mean_temp[year == 1999]

mean_temp_2009 = mean_temp[year == 2009]

mean_temp_2020 = mean_temp[year == 2020]

mean_temp_2009_fil = mean_temp_2009[~np.isnan(mean_temp_2009)]

mean_temp_2020_fil = mean_temp_2020[~np.isnan(mean_temp_2020)]



# Darstellung der Temperaturunterschiede mittels Boxplot
plt.boxplot([mean_temp_1979, mean_temp_1989, mean_temp_1999, mean_temp_2009_fil, mean_temp_2020_fil])
plt.xlabel("Jahr")
plt.xticks([1,2,3,4,5], ["1979", "1989", "1999", "2009", "2020"])
plt.ylabel("Temperatur")
plt.savefig("1_1.png")
plt.show()

#1.2 Zeitlicher Verlauf
plt.plot(mean_temp_2020_fil, "r.")
plt.xlabel("Tag")
plt.ylabel("Temperatur")
plt.savefig("1_2.png")
plt.show()

# 1.3 Herausfinden von Wetterextremen
quant_1979 = np.quantile(mean_temp_1979, 0.5)

quant_1989 = np.quantile(mean_temp_1989, 0.5)

quant_1999 = np.quantile(mean_temp_1999, 0.5)

quant_2009 = np.quantile(mean_temp_2009_fil, 0.5)

quant_2020 = np.quantile(mean_temp_2020_fil, 0.5)

plt.plot(["1979", "1989", "1999", "2009", "2020"],[quant_1979, quant_1989, quant_1999, quant_2009, quant_2020])
plt.xlabel("Jahr")
plt.ylabel("Temperatur Extremwert")
plt.savefig("1_3.png")
plt.show()
# 1.4 Mitelwerte der einzenlen Jahre

years = []
temps = []

for i in range(2011, 2020 + 1):
    years.append(str(i))
    temp = mean_temp[year == i]
    temp_fil = temp[~np.isnan(temp)]
    temp_fil_mean = np.mean(temp_fil)
    temps.append(temp_fil_mean)

plt.bar(years, temps, align='center')
plt.xlabel("Jahr")
plt.xticks([0,1,2,3,4,5,6,7,8,9], ["2011", "2012", "2013", "2014", "2015", "2016", "2017","2018", "2019", "2020"])
plt.ylabel("Temperatur")
#plt.yticks("Temperatur Mittelwert")
plt.savefig("1_4.png")
plt.show()

# 1.5 Weitere Darstellung

years = []
rads = []

for i in range(2011, 2020 + 1):
    years.append(str(i))
    rad = radiation[year == i]
    rad_fil = rad[~np.isnan(rad)]
    rad_fil_mean = np.mean(rad_fil)
    rads.append(rad_fil_mean)

plt.bar(years, rads, align='center')
plt.xlabel("Jahr")
plt.xticks([0,1,2,3,4,5,6,7,8,9], ["2011", "2012", "2013", "2014", "2015", "2016", "2017","2018", "2019", "2020"])
plt.ylabel("Globale Radioaktivität Mittelwert")
plt.savefig("1_5.png")
plt.show()