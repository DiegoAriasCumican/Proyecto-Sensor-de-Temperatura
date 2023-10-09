import numpy as np
import pandas as pd
import pandapower as pp
import pandapower.networks as pn
from pandapower.pf.runpp_3ph import runpp_3ph
import pandapower.plotting as plot
from pandapower.plotting.plotly import simple_plotly
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns
import numpy as np
#Parametros

FP_Residencial=0.9
FP_Industrial=0.85
FP_Comercial=0.88
#############################################################################################################################
#Se genera un dataframe con los valores obtenidos de las graficas
Modelo_Cargas = pd.DataFrame({
    
    'Carga_Residencial': [30,27, 25,23, 20,20, 22,30,40,43,45,51,50,55,60,60,55,50,65,85,100,90,75,55,30],
    
    'Carga_Industrial': [35,33,30,27,25,30,40,55,75,90,100,100,90,100,100,95,90,75,63,55,50,45,40,38,35],
    
    'Carga_Comercial': [22,21,20,21,22,23,25,35,50,65,80,85,90,93,93,88,85,90,100,80,70,60,50,30,20],

    'Hora': ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", 
             "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00",
             "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"]
})
Modelo_Cargas.set_index('Hora', inplace=True)
#############################################################################################################################
#se crea una lista vacia en donde se calculen las potencias necesarias
Potencia_Aparente_Residencial=[]
Potencia_Aparente_Industrial=[]
Potencia_Aparente_Comercial=[]

Potencia_Activa_Residencial=[]
Potencia_Activa_Industrial=[]
Potencia_Activa_Comercial=[]

Potencia_Reactiva_Residencial=[]
Potencia_Reactiva_Industrial=[]
Potencia_Reactiva_Comercial=[]
#############################################################################################################################
#Si se toma la potencia Aparente como 15kVA se obtiene que las listas para la potencia aparente serán:
for i in Modelo_Cargas['Carga_Residencial']:
    nuevo_valor = i*15/100  
    Potencia_Aparente_Residencial.append(nuevo_valor)
    
for i in Modelo_Cargas['Carga_Industrial']:
    nuevo_valor = i*15/100  
    Potencia_Aparente_Industrial.append(nuevo_valor)
    
for i in Modelo_Cargas['Carga_Comercial']:
    nuevo_valor = i*15/100  
    Potencia_Aparente_Comercial.append(nuevo_valor)
    
    
Modelo_Cargas['Potencia_Aparente_Residencial'] = Potencia_Aparente_Residencial
Modelo_Cargas['Potencia_Aparente_Industrial'] = Potencia_Aparente_Industrial
Modelo_Cargas['Potencia_Aparente_Comercial'] = Potencia_Aparente_Comercial

#############################################################################################################################
#Calculo de la potencia activa y su ingreso al dataframe
for i in Modelo_Cargas['Potencia_Aparente_Residencial']:
    nuevo_valor = i*FP_Residencial  
    Potencia_Activa_Residencial.append(nuevo_valor)

for i in Modelo_Cargas['Potencia_Aparente_Industrial']:
    nuevo_valor = i*FP_Industrial 
    Potencia_Activa_Industrial.append(nuevo_valor)
    
for i in Modelo_Cargas['Potencia_Aparente_Comercial']:
    nuevo_valor = i*FP_Comercial 
    Potencia_Activa_Comercial.append(nuevo_valor)

Modelo_Cargas['Potencia_Activa_Residencial'] = Potencia_Activa_Residencial
Modelo_Cargas['Potencia_Activa_Industrial'] = Potencia_Activa_Industrial
Modelo_Cargas['Potencia_Activa_Comercial'] = Potencia_Activa_Comercial
#############################################################################################################################
#Calculo de la potencia reactiva y su ingreso al dataframe

Modelo_Cargas["Potencia_Reactiva_Residencial"]=Modelo_Cargas["Potencia_Aparente_Residencial"]**2-Modelo_Cargas["Potencia_Activa_Residencial"]**2
Modelo_Cargas["Potencia_Reactiva_Residencial"]=Modelo_Cargas["Potencia_Reactiva_Residencial"].apply(np.sqrt)

Modelo_Cargas["Potencia_Reactiva_Industrial"]=Modelo_Cargas["Potencia_Aparente_Industrial"]**2-Modelo_Cargas["Potencia_Activa_Industrial"]**2
Modelo_Cargas["Potencia_Reactiva_Industrial"]=Modelo_Cargas["Potencia_Reactiva_Industrial"].apply(np.sqrt)

Modelo_Cargas["Potencia_Reactiva_Comercial"]=Modelo_Cargas["Potencia_Aparente_Comercial"]**2-Modelo_Cargas["Potencia_Activa_Comercial"]**2
Modelo_Cargas["Potencia_Reactiva_Comercial"]=Modelo_Cargas["Potencia_Reactiva_Comercial"].apply(np.sqrt)



plt.figure(figsize=(12, 6))
plt.gca().set_facecolor('lightgray')
plt.plot(Modelo_Cargas.index, Modelo_Cargas['Carga_Residencial'],label='Residencial', marker='d', color='darkblue')
plt.plot(Modelo_Cargas.index, Modelo_Cargas['Carga_Industrial'],label='Industrial', marker='s', color='deepskyblue')
plt.plot(Modelo_Cargas.index, Modelo_Cargas['Carga_Comercial'],label='Comercial', marker='^', color='yellow')
plt.xlabel('Horas')
plt.ylabel('Demanda (% del Máximo)')
plt.title('Curvas de carga diarias para los tres tipos de carga de las redes BT de referencia')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.9,color='black')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.gca().set_facecolor('lightgray')
plt.plot(Modelo_Cargas.index, Modelo_Cargas['Potencia_Aparente_Residencial'],label='Aparente', marker='d', color='darkblue')
plt.plot(Modelo_Cargas.index, Modelo_Cargas['Potencia_Activa_Residencial'],label='Activa', marker='s', color='deepskyblue')
plt.plot(Modelo_Cargas.index, Modelo_Cargas['Potencia_Reactiva_Residencial'],label='Reactiva', marker='^', color='yellow')
plt.xlabel('Horas')
plt.ylabel('Potencia (kVA)')
plt.title('Potencias Sector Residencial')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.9,color='black')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.gca().set_facecolor('lightgray')
plt.plot(Modelo_Cargas.index, Modelo_Cargas['Potencia_Aparente_Industrial'],label='Aparente', marker='d', color='darkblue')
plt.plot(Modelo_Cargas.index, Modelo_Cargas['Potencia_Activa_Industrial'],label='Activa', marker='s', color='deepskyblue')
plt.plot(Modelo_Cargas.index, Modelo_Cargas['Potencia_Reactiva_Industrial'],label='Reactiva', marker='^', color='yellow')
plt.xlabel('Horas')
plt.ylabel('Potencia (kVA)')
plt.title('Potencias Sector Industrial')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.9,color='black')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.gca().set_facecolor('lightgray')
plt.plot(Modelo_Cargas.index, Modelo_Cargas['Potencia_Aparente_Comercial'],label='Aparente', marker='d', color='darkblue')
plt.plot(Modelo_Cargas.index, Modelo_Cargas['Potencia_Activa_Comercial'],label='Activa', marker='s', color='deepskyblue')
plt.plot(Modelo_Cargas.index, Modelo_Cargas['Potencia_Reactiva_Comercial'],label='Reactiva', marker='^', color='yellow')
plt.xlabel('Horas')
plt.ylabel('Potencia (kVA)')
plt.title('Potencias Sector Comercial')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.9,color='black')
plt.legend()
plt.show()

