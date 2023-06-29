import pandas as pd
import numpy as np

#Lee archivo
archivo = "archivo.xlsx"
df_origen = pd.read_excel(archivo)

#Crea una columna contador y una tabla dinámica la cual los valores nulos se llenan con 0
df_origen["CONTADOR1"] = 1
tabla_dinamica = pd.pivot_table(df_origen, index=['IDTAREA'],columns=["RESULTADO"],values='CONTADOR1', aggfunc='count')
tabla_dinamica = tabla_dinamica.fillna(0)

#Convierte la tabla dinamica a dataframe, en df se almacena todas las columnas a partir de la segunda, es decir las columnas con valores
df_tabla = pd.DataFrame(tabla_dinamica.to_records())
df = df_tabla.iloc[:,1:]
#Cuenta por cada fila los valores que no son cero
df['CONTADOR'] = np.count_nonzero(df.values, axis=1)

#Names son las columnas expresadas en numeros y textos son el nombre de las columnas con el primer caracter en mayuscula
col_num = range(df.shape[1])
col_nombre = df.columns.str.capitalize().values

#Le cambia el nombre a mis columnas y las vuelve numeros con el arreglo names que creé
df.columns = col_num
#Agarro todas las columnas excepto el Contador
df1 = df[col_num[:-1]]
#Algoritmo
textos_completos = []

for z in range(len(df)):
    row1 = df1.iloc[z]
    #Numero de la columnas diferentes a 0
    indexn = row1[row1 != 0].index
    #Se obtiene el nombre de la columna diferente a 0 dado su numero
    texto = [col_nombre[int(i)] for i in indexn]
    #Valor del contador
    row2 = int(df.iloc[z][col_num[-1]])

    if row2 == 1:
        modificadores = ['']
    elif row2 == 2:
        modificadores = [' y ', '']
    else:
        modificadores = [", " for _ in range(row2 - 2)]
        modificadores.extend([' y ', ''])

    textos_modificadores = ''.join([f + b for f, b in zip(texto, modificadores)])
    textos_completos.append(textos_modificadores)

df_tabla["Texto"] = textos_completos
#Excel
df_tabla.to_excel("archivo2.xlsx",index=False)

