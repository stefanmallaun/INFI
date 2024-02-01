import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sp
import seaborn as sb

df = pd.read_csv("INFI\data\european_social_survey\ESS8e02.1_F1.csv", sep=",")
df["gndr"] = pd.cut(df["gndr"], [0,1,2,9], labels=["Male", "Female", "Unspecified"])
gender = df["gndr"]

#1.3 a
trust_police = df["trstplc"]
trust_police_per_gender = pd.crosstab(trust_police, gender, normalize="index")
trust_police_per_gender.plot.bar()
plt.show()

chi, p, dof, expected = sp.chi2_contingency(trust_police_per_gender)
print(chi, "\n", p, "\n", dof, "\n", expected)

sb.heatmap(trust_police_per_gender, annot=False, cmap="YlGnBu")
sb.heatmap(trust_police_per_gender, annot=trust_police_per_gender, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
sb.heatmap(trust_police_per_gender, annot=expected, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
plt.show()

#   Aus dem Diagramm ist ersichtlich, dass diese Aussage nicht stimmt.
#   Tendenziell ist das Vertrauen von Frauen in die Polizei höher
#   Es ist aber auch ersichtlich, dass ein größerer Anteil an Frauen eine Antwort verweigert hat


#1.3 b
negative_correlation_nuclear_sun = df[["elgnuc", "elgsun"]]
df_negative_corr = pd.crosstab(negative_correlation_nuclear_sun["elgnuc"], negative_correlation_nuclear_sun["elgsun"])

corr, p = sp.spearmanr(negative_correlation_nuclear_sun["elgnuc"], negative_correlation_nuclear_sun["elgsun"])
print(corr)

sb.heatmap(df_negative_corr, annot=False, cmap="YlGnBu")
sb.heatmap(df_negative_corr, annot=df_negative_corr, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
sb.heatmap(df_negative_corr, annot=False, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
plt.show()

print("Es gibt einen negativen Zusammenhang zwischen mehr Strom aus nuklearer und solarer Energie" if corr < 0 else "Es gibt einen positiven Zusammenhang zwischen mehr Strom aus nuklearer und solarer Energie" if corr > 0 else "Es gibt keinen negativen Zusammenhang zwischen mehr Strom aus nuklearer und solarer Energie")

#   Durch die Berechnung des Zusammenhanges ist bereits bekannt, dass diese zwei Energiearten (Nucleare Energie und Sonnenkraft) negativ zusammenhängen
#   Ein negativer Zusammenhang bedeutet, dass wenn es von einer dieser Energiequellen mehr Energie gibt, wird weniger von der anderen benötigt.
#   Durch das Diagramm wird dieses Ergebnis zusätzlich bestätigt


#1.3 c
climate_change_feeling = df["ccgdbd"]
countries = df["cntry"].loc[df["cntry"].isin(["AT", "HU"])]
climate_change_feeling_AT_HU = pd.crosstab(climate_change_feeling, countries, normalize="index")
climate_change_feeling_AT_HU.plot.bar()
plt.show()

chi, p, dof, expected = sp.chi2_contingency(climate_change_feeling_AT_HU)
print(chi, "\n", p, "\n", dof, "\n", expected)

sb.heatmap(climate_change_feeling_AT_HU, annot=False, cmap="YlGnBu")
sb.heatmap(climate_change_feeling_AT_HU, annot=climate_change_feeling_AT_HU, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
sb.heatmap(climate_change_feeling_AT_HU, annot=expected, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
plt.show()

#   Aus den uns vorliegenden Daten ist ersichtlich, dass der Klimawandel
#   für Österreicher schlimmer wirkt, als für Menschen aus Ungarn
#   Dies wird durch die Berechung zusätzlich gefestigt



#1.3 d
base_income = df["basinc"]
base_income_per_gender = pd.crosstab(base_income, gender, normalize="index")
base_income_per_gender.plot.bar()
plt.show()

stats, p = sp.mannwhitneyu(base_income.loc[df["gndr"] == "Male"], base_income.loc[df["gndr"] == "Female"])
print(stats, "\n", p,)

sb.heatmap(base_income_per_gender, annot=False, cmap="YlGnBu")
sb.heatmap(base_income_per_gender, annot=base_income_per_gender, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
sb.heatmap(base_income_per_gender, annot=False, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
plt.show()

#   Aus den Daten geht hevor, dass Frauen in der Tate eher einem bedingungslosen Einkommmen zustimmen
#   Diese Tatsache wird besonders bei Betrachtung der Diagramme ersichtlich, da viel mehr Frauen starke Bewertungen (7-9) gegeben haben, als Männer



#1.3 e1
# Hypothesis:
# Deutsche vertrauen dem Europäischen Parlament mehr als Österreicher

trust_in_european_parlament = df["trstep"]#Trust in European Parlament
countries = df["cntry"].loc[df["cntry"].isin(["AT", "DE"])]
trust_in_european_parlament_AT_DE = pd.crosstab(trust_in_european_parlament, countries, normalize="index")
trust_in_european_parlament_AT_DE.plot.bar()
plt.show()

chi, p, dof, expected = sp.chi2_contingency(trust_in_european_parlament_AT_DE)
print(chi, "\n", p, "\n", dof, "\n", expected)

sb.heatmap(trust_in_european_parlament_AT_DE, annot=False, cmap="YlGnBu")
sb.heatmap(trust_in_european_parlament_AT_DE, annot=trust_in_european_parlament_AT_DE, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
sb.heatmap(trust_in_european_parlament_AT_DE, annot=expected, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
plt.show()

#   Bei einer Untersuchung des Vertrauens von Deutschen und Österreicher in das Europäische Patlament stellt sich heraus:
#   Deutsche vertrauen dem Europäische Parlament mehr als Österreicher.
#   Es fällt ebenfalls auf, dass viele Österreicher diese Frage abgelehnt haben und dass mehr Deutsche die Antwort dazu nicht wussten.


#1.3 e2
# Hypothesis:
# Franzosen vertrauen den Vereinten Nationen weniger als Österreicher
trust_in_united_nations = df["trstun"]# Trust in United Nations
countries = df["cntry"].loc[df["cntry"].isin(["AT", "FR"])]
trust_in_united_nations_AT_FR = pd.crosstab(trust_in_united_nations, countries, normalize="index")
trust_in_united_nations_AT_FR.plot.bar()
plt.show()

chi, p, dof, expected = sp.chi2_contingency(trust_in_united_nations_AT_FR)
print(chi, "\n", p, "\n", dof, "\n", expected)

sb.heatmap(trust_in_united_nations_AT_FR, annot=False, cmap="YlGnBu")
sb.heatmap(trust_in_united_nations_AT_FR, annot=trust_in_united_nations_AT_FR, annot_kws={'va':'bottom'}, fmt="", cbar=False , cmap="YlGnBu")
sb.heatmap(trust_in_united_nations_AT_FR, annot=expected, annot_kws={'va':'top'}, fmt=".2f", cbar=False, cmap="YlGnBu")
plt.show()

#   Aus dem Diagramm geht hervor, dass Österreicher sehr gespalten zwischen wenig und kompletten Vertrauen sind.
#   Man sieht auch, dass mehr Österreicher diese Frage abgelehnt oder nicht gewusst haben