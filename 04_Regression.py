import numpy as np
import pandas as pd
import statsmodels.api as sm
from matplotlib import pyplot as plt

df = pd.read_excel("INFI\\data\\bev_meld.xlsx")

# 2.1
growth = df.values[:,3:].sum(axis=0)
plt.title("Gesamtbevölkerung pro Jahr")
plt.plot(df.columns[3:], growth)
plt.xlabel("Jahr")
plt.ylabel("Bevölkerungszahl")
#plt.savefig("img/2_1.png")
plt.show()

# 2.2
def get_model(y, v):
    df_req = pd.DataFrame({"years": y, "bev": v})
    model = sm.OLS.from_formula("bev ~ years", df_req).fit()
    return model

def predict_growth(y, v, year):
    model = get_model(y, v)
    print(model.summary())
    return str(model.params[1] * year + model.params[0])

print("Prognose 2030: " + predict_growth(pd.to_numeric(df.columns[3:]), pd.to_numeric(growth), 2030))
plt.plot(np.arange(2030, 2100), get_model(pd.to_numeric(df.columns[3:]), pd.to_numeric(growth)).predict(pd.DataFrame({"years": np.arange(2030, 2100)})))
plt.title("Prognose 2030 - 2100")
#plt.savefig("img/2_2.png")
plt.show()

# zu 5 Erkenntnisse:
# Als Wachstum wird hier der Mittelwert des Bevölkerungswachstums pro Jahr verwendet
# Das Diagramm stellt also nicht das genaue Wachstum der Bevölkerungszahl dar, zeigt aber, dass die Bevölkerung, basierend auf dem bisherigen Trend weiterwachsen wird.


# 3
print("Prognose Wörgl 2030: " + predict_growth(pd.to_numeric(df.columns[3:]), pd.to_numeric(df.values[139, 3:]), 2030))
plt.plot(np.arange(2030, 2100), get_model(pd.to_numeric(df.columns[3:]), pd.to_numeric(df.values[139, 3:])).predict(pd.DataFrame({"years": np.arange(2030, 2100)})))
plt.title("Prognose Wörgl 2030 - 2100")
#plt.savefig("img/3")
plt.show()

# zu 5 Erkenntnisse:
# Als Wachstum wird hier der Mittelwert des Bevölkerungswachstums von Angerberg pro Jahr verwendet
# Das Diagramm stellt also nicht das genaue Wachstum der Bevölkerungszahl dar, zeigt aber, dass die Bevölkerung, basierend auf dem bisherigen Trend weiterwachsen wird.


# 4
figure, axi = plt.subplots(2, 1)
t1 = df.values[25:89, 3:].sum(axis=0)
d1 = pd.DataFrame({"Bevölkerungszahl": t1})
t2 = df.values[110:139, 3:].sum(axis=0)
d2 = pd.DataFrame({"Bevölkerungszahl":t2})

d1.plot(ax = axi[0], title = "Gemeinde IL")
d2.plot(ax = axi[1], title = "Gemeinde KU")

figure.tight_layout()
#plt.savefig("img/4_1")
plt.show()

# 4.2
plt.plot(df.columns[3:], d1, label = "IL")
plt.plot(df.columns[3:], d2, label = "KU")
plt.legend()
#plt.savefig("img/4_2")

# 4.3
plt.plot(df.columns[3:], get_model(pd.to_numeric(df.columns[3:]),pd.to_numeric(df.values[25:89, 3:].sum(axis=0))).predict(pd.DataFrame({"years": np.arange(1993, 2022)})), label="IL")
plt.plot(df.columns[3:], get_model(pd.to_numeric(df.columns[3:]),pd.to_numeric(df.values[110:139, 3:].sum(axis=0))).predict(pd.DataFrame({"years": np.arange(1993, 2022)})), label="KU")
plt.legend()
#plt.savefig("img/4_3")
plt.show()

# zu 5 Erkenntnisse:
# Hier ist hut zu sehen, dass die Regressionsgerade nicht weit von den tatsächlichen Werten abweicht, was besonders bei Kufstein der Fall ist.
# Bei Innsbruck Land weicht die Regressionsgerade etwas weiter von den gemessenen Werten ab, ist aber trotzdem relativ genau.