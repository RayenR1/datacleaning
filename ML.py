from ucimlrepo import fetch_ucirepo 
import pandas as pd

# fetch dataset 
myocardial_infarction_complications = fetch_ucirepo(id=579) 

# data (as pandas dataframes) 
X = myocardial_infarction_complications.data.features 
y = myocardial_infarction_complications.data.targets 



Z = pd.concat([X, y], axis=1)  

# Vérifier les données
print(Z.head())  

# Exporter les données
with open("C:/Users/jlassi/Desktop/ML projet/datasettarget.csv", "w", newline="") as f:
    y.to_csv(f, index=False)
    print("Les données ont été exportées avec succès")
