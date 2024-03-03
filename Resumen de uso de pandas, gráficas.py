# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 18:36:38 2023

@author: eduar
"""

"RESUMEN DE PANDAS"
# Manejar y analizar datos con dataframes de pandas


#impotación de librería
import pandas as pd

# Creación de una dataframe con listas

#etiquetas
nombre_paises = ["China", "India", "Estados Unidos", "indonesia", "Pakistan",
                 "Brasil", "Nigeria", "Bangladesh", "Rusia", "México"]
#nombre de columnas
encabezado = ["Poblacion", "Porcentaje"]
#datos
datos = [[1439, 18.47], [1380, 17.70], [331, 4.25], [273, 3.51], [220, 2.83],
         [212, 2.73], [206, 2.64], [164, 2.11], [145, 1.87], [128, 1.65]]

#dataframe sin encabezados
paises = pd.DataFrame(datos)
paises

########################################################
#Dataframe con encabezado e indices
paises = pd.DataFrame(datos, index=nombre_paises, columns=encabezado)
paises #cada columna del dataframe es una serie


#Dataframe con diccionario
datos = {
    "China": [1439, 18.47],
    "India": [1380, 17.70],
    "Estados Unidos": [331, 4.25],
    "Indonesia": [273, 3.51],
    "Pakistan": [220, 2.83],
    "Brasil":[212, 2.73],
    "Nigeria": [206, 2.64],
    "Bangladesh": [164, 2.11],
    "Rusia": [145, 1.87],
    "México": [128, 1.65]
    }

paises = pd.DataFrame(datos) #convertir en dataframe
paises # es un dataframe TRANSPUESTO

paises = pd.DataFrame(datos, index=encabezado) #agregar index
paises
#transponer los datos
paises = paises.transpose() #paises = paises.T 
paises

#####################################################
data = pd.read_csv("C:/Users/eduar/OneDrive/Escritorio/Ejercicios Python/datos_ejercicios.csv")
data.head()

#tamaño de filas y columnas
print(data.shape) 

#Seleccionar solo las columnas a usar
data_clean = data[["ANIO_GASTO", "MES_GASTO", "cliente", "Edad", "Genero", "Gasto",
                   "ENTIDAD", "DH", "Tipo_empleado", "medicamento", "fecha_completa"]]
#Atributos básicos de un dataframe

#tipo de datos:
paises.dtypes

#acceder a valores
paises.values #ver solo valores sin encabezados

#tamaño del dataframe, total de celdas/elementos
paises.size

#indice del dataframe
paises.index

#columnas del datafrmae
paises.columns

#####################################################
#Acceso a los valores(columnas o filas) del dataframe

# Acceder a columnas
paises.Poblacion
#otra forma es
paises["Poblacion"]

#ver varias columnas
paises[["Poblacion", "Porcentaje"]]

#Acceder a filas
paises["Poblacion"][1] #acceder a columna "Población" en FILA 2
paises.Poblacion[1] #lo mismo que arriba; acceder a columna y fila específica
paises["Poblacion"][0:3] #acceder a columna POBLACION de la fila 0 a la 2

# Aceeder con "iloc" y "loc"
paises.iloc[0]#acceder a toda la fila 1, que tiene index 0=CHINA
paises.loc["China"] #acceder a toda la fina 1, que tiene index CHINA



####################################################################
#Métodos de dataframe

#convertir un tipo de dato a otro tipo de dato

#información de dataframe
paises.info()

#convertir de float a int
paises["Poblacion"] = paises["Poblacion"].astype("int")
paises

#ver primeros renglones del datafram
paises.head() #ver primeros 5
paises.head(7) #ver primeros 7

#ver últimas filas del dataframe
paises.tail() #ver últimas 5 filas
paises.tail(3) #ver últimas 3 filas

#ordenar el dataframe de acuerdo a columnas deseadas
paises.sort_values(by=["Porcentaje", "Poblacion"],
                  ascending=True) #odernar primero por porcwentaje y despues por poblacion
#ordenar el dataframe de acuerdo al index
paises.sort_index()

####################################################################
#agregar y borrar columnas

#agregar una nueva columna
tasa_fertilidad = [1.7, 2.2, 1.8, 2.3, 3.6, 1.7, 5.4, 2.1, 1.8, 2.1] #nueva columnas
paises["Tasa_fertilidad"]= tasa_fertilidad #agregación de nueva columna
paises

#eliminar columnas con pop
paises.pop("Tasa_fertilidad") #muestra columna eliminada
paises

#eliminar columna con del
del paises["Tasa_fertilidad"] #elegir columna a eliminar
paises

#eliminar columna con DROP; eliminar columnas: AXIS=1; y filas=AXIS=0
paises.drop("Tasa_fertilidad", axis=1, inplace=True)
paises

#agregar columna de un dataframe CSV
data_clean["new_col"]= (
    data_clean["Gasto"] / data_clean["Edad"]
    )
data_clean.head()

#Eliminar la columna de un dataframe CSV
del (data_clean["new_col"])
data_clean.head()
#Eliminar varias columnas de un dataframe CSV
data_clean1 = data_clean.drop(["medicamento", "fecha_completa", "Edad",
                               "MES_GASTO", "ANIO_GASTO"], axis=1)
data_clean1

#Eliminar filas de un dataframe CSV
data_clean.drop(4) #Eliminar fila con idex 4
#eliminar filas con un rango
data_clean.drop(range(0,10)) #eliminar filas entre rango INDEX de 0 a 10


#
#Eliminar renglon, considerando que se tiene un INDEX de nombre de paises
renglon = pd.Series(name="Japón", data=[126, 1.62], index=["Poblacion", "Porcentaje"])
renglon

#agregar el renglon/fila
paises = paises.append(renglon) #se agregó al final el nuevo ROW
paises

#Eliminar filas con DROP

paises.drop(["México", "Japón"], axis=0, inplace=True) #elimina filas con index MEXICO, JAPON
paises


######################################################################
#funciones de estadística y de agregación

# estadística básica
paises.describe()

# mínimo de las columnas
paises.min()
paises.mean()
paises.mode()

#Suma acumulativa
paises.cumsum()

#gráfica de bigotes
paises.boxplot()




#########################################################################################
# Limpieza de datos

# importación de liberías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#importar archivo CSV
data = pd.read_csv("C:/Users/eduar/OneDrive/Escritorio/Ejercicios Python/datos_ejercicios.csv")
data.head()

#tamaño de filas y columnas
print(data.shape) 

#Seleccionar solo las columnas a usar
data_clean = data[["ANIO_GASTO", "MES_GASTO", "cliente", "Edad", "Genero", "Gasto",
                   "ENTIDAD", "DH", "Tipo_empleado", "medicamento", "fecha_completa"]]

#tipo de datos del dataframe
data_clean.info()


# Eliminar datos faltantes, aplicar solo cuando los datos faltantes son pocos
data_clean.dropna(inplace=True)
data_clean.info() #se elinaron los NaN, todas las columnas tinen mismo num de filas

#reordenamiento de las filas del datafrme
data_clean.head()
data_clean.sample(frac=1)
data_clean=data_clean.sample(frac=1)
data_clean



# Eliminar columnas irrelevantes; depende de lo que se quiere analizar
# eje: columna con info redundante, columna de STRING, columna con un solo valor, 

#Ver subcategorías de las columnas categóricas
columnas_categoricas = ["cliente", "Genero", "ENTIDAD", "DH", "Tipo_empleado",
                        "medicamento"]

#valor de un dataframe
data_clean.values

#mostrar número de subctegorías en cada columna categórica:
for sub_categorias in columnas_categoricas:
    print(f"Columna {sub_categorias}: {data_clean[sub_categorias].nunique()} subniveles")

#Eliminar filas duplciadas
print(f"Tamaño del set antes de eliminar las filas repetidas: {data_clean.shape}")
data_clean.drop_duplicates(inplace=True)
print(f"Tamaño del set después de eliminar filas repetidas: {data_clean.shape}")

#######################################################################################

#Filtrar filas y columnas

#filtrar filas con índices, primeros 20 filas
data_clean[0:20]
data_clean[100:110]


#Filtrar una columna del dataframe
data_clean["cliente"]

#filtrar más de una columna
data_clean[["cliente", "Tipo_empleado", "Gasto"]]

#Filtrar filas que son del cliente santander
SANTANDER = data_clean[data_clean["cliente"]=="SANTANDER"]
SANTANDER.head()

gasto_alto = data_clean[data_clean["Gasto"]>=12000]
gasto_alto

#filtrar por dos categorías
mes_1_12 = data_clean[data_clean["MES_GASTO"].isin([1,12])]
mes_1_12 = data_clean[(data_clean["MES_GASTO"]==1) | (data_clean["MES_GASTO"]==12)]
mes_1_12

data_clean[(data_clean["DH"] == "Titular") & (data_clean["ANIO_GASTO"]==2022) 
           & (data_clean["Gasto"]>=11000)]

data_clean[data_clean.ENTIDAD.isin(["Colima", "Campeche", "Veracruz", "Sonora"]) 
   & (data_clean["Gasto"]> 1000)]


#filtrar que no están vaciós en MES_GASTO
no_mes = data_clean[data_clean["MES_GASTO"].notna()]
no_mes

#filtrado con iloc[FILAi:FILAf, COLUMNA1:COLUMNAf] y LOC["nameFILAi":"nameFILAf", "INDEX_COLUMNAi":"INDEX_COLUMNAf"]

#filtrar filas 1 al 25 con todas las columnas
data_clean.iloc[0:4, :]

#filtrar primeras 10 filas con las 3 primeras columnas
data_clean.iloc[0:10, 0:3]

#filtrar una columna y mostrar solo UNA otra columna
gasto_santander = data_clean.loc[data_clean["cliente"]=="SANTANDER", ["Gasto"]]
gasto_santander

#mostrar primeras 10 filas de columna 5 al 8
data_clean.iloc[0:10, 5:9]


#filtrar filas y obtener estadística
data_clean[data_clean["DH"]=="Titular"].mean()
data_clean[data_clean["cliente"]=="SANTANDER"].max()


#unir dos tablas
table1= data_clean[data_clean.cliente=="SANTANDER"]
table2 = data_clean[data_clean.cliente=="EDPM"]
table1

table_1y2 = table1.append(table2)
table_1y2

##########################
#uso de GROUP BY
data_clean.groupby(by = "ENTIDAD")["Gasto"].sum() #agrpar suma de gasto por cliente
data_clean.groupby(by = "ENTIDAD")["Edad"].mean() #agrupar edad promedio por ENTIDAD
data_clean.groupby(by = "cliente")["Genero"].count()
data_clean.groupby(by = "cliente")["Gasto"].describe()
data_clean.groupby(by="ENTIDAD")["Gasto", "Edad"].mean()
data_clean.groupby(by="cliente")["Gasto", "Edad"].max()
data_clean.groupby(by="cliente")["Gasto", "Edad"].max() - data_clean.groupby(by="cliente")["Gasto", "Edad"].min()
data_clean.groupby(by=["DH", "cliente"])["Gasto"].mean()
data_clean.groupby(by=["DH", "cliente"])["Gasto", "Edad"].mean()
my_groupby = data_clean.groupby(by=["DH", "cliente"])["Gasto", "Edad"].max()
my_groupby
#######################################################
#Eliminar datos duplicados


















#Outliers en las variables numéricas

#generar gráficos individuales para cada variable
columnas_numericas = ["ANIO_GASTO", "MES_GASTO", "Edad", "Gasto"]

fig, ax = plt.subplots(nrows=4, ncols=1, figsize=(8,30))
fig.subplots_adjust(hspace=0.5)

for i, col in enumerate(columnas_numericas):
    sns.boxplot(x=col, data=data_clean, ax=ax[i])
    ax[i].set_title(col)

# con lo anterio se observa que en GASTO hay outliers, eliminarlos
#Quedarnos solo con los datos que exlucyan los mayores a 12500 y menores a 7500
print(f"Tamaño del set antes de eliminar registros de gasto mayor a 12.5mil y menor a 8mil: {data_clean.shape}")
data_clean = data_clean[(data_clean["Gasto"]<= 12500) & (data_clean["Gasto"]>=7500)]
print(f"Tamaño del set después de eliminar registros de gasto mayor a 12mil y menor a 8mil: {data_clean.shape}")

sns.boxplot(data=data_clean["Gasto"]) #ya no hay outliers
##################
# Errores tipográficos en variables categóricas
columnas_categoricas = ["cliente", "Genero", "ENTIDAD", "DH", "Tipo_empleado",
                        "medicamento"]
#graficas las varibales categóricas
fig, ax = plt.subplots(nrows=6, ncols=1, figsize=(10,30))
fig.subplots_adjust(hspace=1)

for i, col in enumerate(columnas_categoricas):
    sns.countplot(x=col, data=data_clean, ax=ax[i])
    ax[i].set_title(col)
    ax[i].set_xticklabels(ax[i].get_xticklabels(), rotation=30)


# con la gráfica anterio observamos que en GENERO: h=HOMBRE=MASUCULINO...
#convertir las subcategorías en Mayúsculas - minúsculas
for columna in data_clean.columns:
    if columna in columnas_categoricas:
        data_clean[columna]=data_clean[columna].str.lower()
#unificar GENERO
print(data_clean["Genero"].unique())
data_clean["Genero"]=data_clean["Genero"].str.replace("mujer", "femenino")
data_clean["Genero"]=data_clean["Genero"].str.replace("hombre", "masculino")
data_clean["Genero"]=data_clean["Genero"].str.replace("h", "masculino")
print(data_clean["Genero"].unique())

#unificar medicmaentos
print(data_clean["medicamento"].unique())
data_clean[data_clean["medicamento"]=="patete"]="patente" #remplazar patete con patente
data_clean[data_clean["medicamento"]=="generio"]="generico" #remplazar patete con patente
print(data_clean["medicamento"].unique())

##############################################################################
# Análisis exploratorio con python

# importación de liberías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#importar archivo CSV
data = pd.read_csv("C:/Users/eduar/OneDrive/Escritorio/Ejercicios Python/datos_ejercicios.csv")
data.head()

#Seleccionar solo las columnas a usar
data_clean = data[["ANIO_GASTO", "MES_GASTO", "cliente", "Edad", "Genero", "Gasto",
                   "ENTIDAD", "DH", "Tipo_empleado", "medicamento", "fecha_completa"]]

#tipo de datos del dataframe
data_clean.info()


# Eliminar datos faltantes, aplicar solo cuando los datos faltantes son pocos
data_clean.dropna(inplace=True)
data_clean.info() #se elinaron los NaN, todas las columnas tinen mismo num de filas

# A) Análisis individual de cada variable
# ver tipo de cada viarbale
data_clean.info() # object son CATEGÓRICAS y float son NUMÉRICAS

#graficar variables categóricas:
columnas_categoricas = ["cliente", "Genero", "ENTIDAD", "DH", "Tipo_empleado",
                        "medicamento"]
#graficas las varibales categóricas
fig, ax = plt.subplots(nrows=6, ncols=1, figsize=(10,30))
fig.subplots_adjust(hspace=1)
for i, col in enumerate(columnas_categoricas):
    sns.countplot(x=col, data=data_clean, ax=ax[i])
    ax[i].set_title(col)
    ax[i].set_xticklabels(ax[i].get_xticklabels(), rotation=30)    

#mostrar número de subctegorías en cada columna categórica:
for sub_categorias in columnas_categoricas:
    print(f"Columna {sub_categorias}: {data_clean[sub_categorias].nunique()} subniveles")

"""Columna cliente: 5 subniveles
    Columna Genero: 5 subniveles
    Columna ENTIDAD: 32 subniveles
    Columna DH: 2 subniveles
    Columna Tipo_empleado: 2 subniveles
    Columna medicamento: 4 subniveles"""

# ver columnas numéricas
data_clean.describe()

# histograma de GASTO y EDAD
columna_n = ["Gasto", "Edad"]
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,30))
fig.subplots_adjust(hspace=0.5)
for i, col in enumerate(columna_n):
    if col == "Edad":
        nbins=10
    else:
        nbins=50
    sns.histplot(x=col, data=data_clean, ax=ax[i], bins=nbins, kde=True)
    ax[i].set_title(col)
    
data_clean["Gasto"].describe()    
    
# B) Análisis univariado: relación de cada variable predictora con la variabl a predecir
# Analizar una variable: ¿Tasa de FEMENINOS y MASCULINOS?
data_clean["Genero"].unique()
diccionario_genero = { #Masuclino:1, Femenino:0
    "Femenino":0,
    "Masculino":1,
    "Hombre":1,
    "H":1,
    "Mujer":0
    }
genero_numero = data_clean["Genero"].map(diccionario_genero)
data_clean["Genero_binario"]=genero_numero
data_clean["Genero_binario"].unique()
data_clean.head()

#analizar relación entre variable numérica y la variable a predecir (MASCULINO o FEMENINO)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,55))
fig.subplots_adjust(hspace=0.25)

for i, col in enumerate(columnas_categoricas):
    bptl = sns.boxplot(x = "Genero_binario", y=col, data=data_clean, ax=ax[i])
    ax[i].set_xlabel("Genero binario (1: Masculino, 0:Femenino)")
    ax[i].set_title(col)
    

#convertir el gasto en rangos
data_clean["Gasto"].describe()    
data_clean.loc[:, "Gasto_rango"]= "<0"  #crear una columna "Gasto_rango" donde todos son "<900"
data_clean.loc[(data_clean["Gasto"]>0) & (data_clean["Gasto"]<= 9000), "Gasto_rango"] = "0-9000"
data_clean.loc[(data_clean["Gasto"]>9000) & (data_clean["Gasto"]<=11000), "Gasto_rango"] = "9001-11000"
data_clean.loc[(data_clean["Gasto"]>11000) & (data_clean["Gasto"]<=12500), "Gasto_rango"] = "11001-12500"
data_clean.loc[data_clean["Gasto"]>12500, "Gasto_rango"] = ">125001"    
data_clean.head()
data_clean["Gasto_rango"].unique()


# C) Análisis bivariado: relación de pares de variables predictoras con la variable a predecir
#análisis de de dos variables




####################################################################################
# Visualización de datos
# importación de liberías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#importar archivo CSV
data = pd.read_csv("C:/Users/eduar/OneDrive/Escritorio/Ejercicios Python/datos_ejercicios.csv")
data.head()

#Seleccionar solo las columnas a usar
data_clean = data[["ANIO_GASTO", "MES_GASTO", "cliente", "Edad", "Genero", "Gasto",
                   "ENTIDAD", "DH", "Tipo_empleado", "medicamento", "fecha_completa"]]

#tipo de datos del dataframe
data_clean.info()


# Eliminar datos faltantes, aplicar solo cuando los datos faltantes son pocos
data_clean.dropna(inplace=True)
data_clean.info() #se elinaron los NaN, todas las columnas tinen mismo num de filas



# Scatter plot
plt.scatter(x=data_clean["Edad"], y=data_clean["Gasto"])
plt.title("Gráfica de desipersión de edad contra gasto")
plt.xlabel("Edad del derechohabiente")
plt.ylabel("Gasto mensual del DH")
plt.show()

plt.scatter(x=data_clean["Edad"], y=data_clean["Gasto"], c=data_clean["ANIO_GASTO"], # c es para color de bolitas
            s=data_clean["MES_GASTO"])
plt.title("Gráfica de desipersión de edad contra gasto")
plt.xlabel("Edad del derechohabiente")
plt.ylabel("Gasto mensual del DH")
plt.colorbar()
plt.show()


# scatter plot con color
plt.style.use("ggplot")
data_clean.plot.scatter(x="Edad", y="Gasto",  color="blue", marker="*")
plt.title("Gráfica de dispersión de edad contra gasto")
plt.xlabel("Edad del derechohabiente")
plt.ylabel("Gasto mensual del DH")
plt.show()


from re import S
data_clean.plot.scatter(x="Edad", y="Gasto",  c=data_clean["ANIO_GASTO"], 
                        s=data_clean["MES_GASTO"])
plt.title("Gráfica de dispersión de edad contra gasto")
plt.xlabel("Edad del derechohabiente")
plt.ylabel("Gasto mensual del DH")
plt.show()

# Gráfica de líneas LINE CHART
data_clean.columns
plt.plot(data_clean["Edad"]) 
plt.plot(data_clean["Gasto"])
plt.title("Gráfica de edad vs gasto") # título de gráfica
plt.xlabel("Edad") #título del eje x
plt.ylabel("Gasto") #título del eje y
plt.show()


#gráfic de barras BAR CHART
plt.bar(data_clean["cliente"], data_clean["Gasto"], color="red")
plt.title("Gasto por cliente") #título de la gráfica
plt.xlabel("Clientes") #etiqueta del eje x
plt.ylabel("Gasto mensual del clinete") # etiqueta del eje y
plt.show() #ver gráfica


#gráfica de barras y de línea

ax = data_clean.plot.bar("fecha_completa", "Edad", color="green")
data_clean.plot.line("fecha_completa", "Gasto", secondary_y=True, ax=ax, color="red")
ax.set_xlim((1, 15))


# Histograma / Histogram
plt.hist(data_clean["Gasto"], color="pink") #seleccionar varibale
plt.title("Histograma de gasto mensual") # t´titulo de la gráfica
plt.ylabel("Count/frecuencia de gasto")
plt.xlabel("Gasto mensual por rango")
plt.show() #ver gráfica



# visualización con SEABORN
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Draw lineplot
sns.lineplot(x="fecha_completa", y="Gasto", data=data_clean, color="blue") 
plt.title('Gráfica lineal del gasto mensual usando seaborn') #t´titulo de la gráfica
plt.show() #ver gráfica

#scatter plot
sns.scatterplot(x="Edad", y="Gasto", data=data_clean, color="green",) 
plt.title('Gráfica lineal del gasto mensual usando seaborn')
plt.show()


sns.scatterplot(x="Edad", y="Gasto", data=data_clean, color="green", hue="Tipo_empleado") 
plt.title('Gráfica lineal del gasto mensual usando seaborn')
plt.show()

#line plot, graficanto todo menos el ANIO_GASTO
sns.lineplot(data=data_clean.drop(["ANIO_GASTO"], axis=1)) 
plt.title('Gráfica lineal del gasto mensual usando seaborn')
plt.show()

#bar plot
sns.barplot(x="MES_GASTO", y="Gasto", data=data_clean, hue="DH")
plt.title("Gráfica de barras del gasto por mes con seaborn") #título de la gráfica
plt.xlabel("Mes del gasto") #etiqueta del eje x
plt.ylabel("Gsasto en miles de pesos") # etiqueta del eje y
plt.show() #ver gráfica


# histogram
sns.histplot(x="Gasto", data=data_clean, kde=True, hue="DH",) 
plt.title("Histograma del gasto  con seaborn") 
    # kde=True indica si se agrega línea
    #hue="smoker" indica si se difefenciasn entre otra variable categorica
plt.show()

###################
data = pd.read_csv("C:/Users/eduar/OneDrive/Escritorio/Ejercicios Python/datos_ejercicios.csv")
data.head()

#Seleccionar solo las columnas a usar
data_clean = data[["ANIO_GASTO", "MES_GASTO", "cliente", "Edad", "Genero", "Gasto",
                   "ENTIDAD", "DH", "Tipo_empleado", "medicamento", "fecha_completa"]]

# Eliminar datos faltantes, aplicar solo cuando los datos faltantes son pocos
data_clean.dropna(inplace=True)
data_clean.info()
#una gráfica
data_clean=data_clean.sort_values(by=["fecha_completa"], ascending=True)
data_clean.head(30)
plt.plot(data_clean["fecha_completa"], data_clean["Gasto"])
plt.show()


#dos gráficas en una misma gráfica
plt.plot(data_clean["fecha_completa"], data_clean["Gasto"])
plt.plot(data_clean["fecha_completa"], data_clean["Edad"]*100)
plt.show()

#Personalización de gráficas en matplot
plt.plot(data_clean["fecha_completa"], data_clean["Gasto"]/100, color="green", 
         label="Gasto en miles", marker="^")#línea 1
plt.plot(data_clean["fecha_completa"], data_clean["Edad"], color="black", 
         label="Edad", marker="*")#línea 2
plt.plot(data_clean["fecha_completa"], data_clean["MES_GASTO"]*10, color="red", 
         label="MES de gasto", marker="+")#línea 3
plt.legend() #activar la visualización de las leyendas anteriores
plt.title("Gasto, edad y mes de la efectuación del gasto") #título
plt.xlabel("Fecha completa del gasto") #título eje X
plt.ylabel("Gasto, edad y mes*10")
plt.yticks(range(20,135,10)) #Personalizar escala del eje Y, por ejemplo de 20 a 120 de 10 en 10
plt.grid() #agregar cuadrícula
plt.minorticks_on() #activar marcar menores en los ejes
plt.show()

plt.plot(data_clean["fecha_completa"], data_clean["Gasto"]/100, color="green", 
         label="Gasto en miles", linestyle="-")#línea 1
plt.plot(data_clean["fecha_completa"], data_clean["Edad"], color="black", 
         label="Edad", linestyle="-.")#línea 2
plt.plot(data_clean["fecha_completa"], data_clean["MES_GASTO"]*10, color="red", 
         label="MES de gasto", linestyle=":")#línea 3
plt.legend() #activar la visualización de las leyendas anteriores
plt.title("Gasto, edad y mes de la efectuación del gasto") #título
plt.xlabel("Fecha completa del gasto") #título eje X
plt.ylabel("Gasto, edad y mes*10")
plt.yticks(range(20,135,10)) #Personalizar escala del eje Y, por ejemplo de 20 a 120 de 10 en 10
plt.grid() #agregar cuadrícula
plt.minorticks_on() #activar marcar menores en los ejes
plt.show()

################# gráficas de barras verticales
plt.bar(data_clean["ANIO_GASTO"]+0.2, data_clean["Gasto"]/100, color="green", 
         label="Gasto en miles", width=1/3)#línea 1 // las sumade DECIMALES ayuda a ver que no se tapen las barras
plt.bar(data_clean["ANIO_GASTO"]+0.4, data_clean["Edad"], color="black", 
         label="Edad", width=1/3)#línea 2 // WIDTH es para la anchura de la barra
plt.bar(data_clean["ANIO_GASTO"]+0.6, data_clean["MES_GASTO"]*10, color="red", 
         label="MES de gasto", width=1/3 )#línea 3
plt.legend() #activar la visualización de las leyendas anteriores
plt.title("Gasto, edad y mes de la efectuación del gasto") #título
plt.xlabel("Fecha completa del gasto") #título eje X
plt.ylabel("Gasto, edad y mes*10")
plt.grid() #agregar cuadrícula
plt.show()

################# gráficas de barras horizontales
plt.barh(data_clean["ANIO_GASTO"]+0.2, data_clean["Gasto"]/100, color="green", 
         label="Gasto en miles", height=1/3)#línea 1 // las sumade DECIMALES ayuda a ver que no se tapen las barras
plt.barh(data_clean["ANIO_GASTO"]+0.4, data_clean["Edad"], color="black", 
         label="Edad", height=1/3)#línea 2 // height es para la anchura de la barra
plt.barh(data_clean["ANIO_GASTO"]+0.6, data_clean["MES_GASTO"]*10, color="red", 
         label="MES de gasto", height=1/3 )#línea 3
plt.legend() #activar la visualización de las leyendas anteriores
plt.title("Gasto, edad y mes de la efectuación del gasto") #título
plt.xlabel("Fecha completa del gasto") #título eje X
plt.ylabel("Gasto, edad y mes*10")
plt.grid() #agregar cuadrícula
plt.show()

############### gráfica de barras verticales apiladas

plt.bar(data_clean["ANIO_GASTO"], data_clean["Gasto"]/100, color="green", 
         label="Gasto en miles", )#línea 1 // las sumade DECIMALES ayuda a ver que no se tapen las barras
plt.bar(data_clean["ANIO_GASTO"], data_clean["Edad"], color="black", 
         label="Edad", bottom=data_clean["Gasto"]/100)#línea 2 // WIDTH es para la anchura de la barra
plt.bar(data_clean["ANIO_GASTO"], data_clean["MES_GASTO"]*10, color="red", 
         label="MES de gasto", bottom=data_clean["Gasto"]/100+data_clean["Edad"])#línea 3
plt.legend() #activar la visualización de las leyendas anteriores
plt.title("Gasto, edad y mes de la efectuación del gasto") #título
plt.xlabel("Fecha completa del gasto") #título eje X
plt.ylabel("Gasto, edad y mes*10")
plt.grid() #agregar cuadrícula
plt.show()

#gráfica de dispersión
plt.scatter(data_clean["MES_GASTO"], data_clean["Gasto"]/100, color="green", 
         label="Gasto en miles", marker="^")#línea 1
plt.scatter(data_clean["MES_GASTO"], data_clean["Edad"], color="black", 
         label="Edad", marker="*")#línea 2
plt.scatter(data_clean["MES_GASTO"], data_clean["MES_GASTO"]*10, color="red", 
         label="MES de gasto", marker="+")#línea 3
plt.legend() #activar la visualización de las leyendas anteriores
plt.title("Gasto, edad y mes de la efectuación del gasto") #título
plt.xlabel("Fecha completa del gasto") #título eje X
plt.ylabel("Gasto, edad y mes*10")
plt.yticks(range(20,135,10)) #Personalizar escala del eje Y, por ejemplo de 20 a 120 de 10 en 10
plt.show()

#Gráfica de PIE
plt.pie(data_clean["ANIO_GASTO"], labels=data_clean["Genero"])
plt.show()
# Combiar distintas gráficas
plt.bar(data_clean["MES_GASTO"], data_clean["Gasto"]/100, width=1/3)
plt.bar(data_clean["MES_GASTO"]+0.2, data_clean["Edad"], width=1/3)
plt.plot(data_clean["Edad"], data_clean["Gasto"]/100)
plt.scatter(data_clean["MES_GASTO"], data_clean["Gasto"]/100)
plt.scatter(data_clean["MES_GASTO"], data_clean["Edad"])
plt.show()

########### visualización con BOKEH
pip install jinja2==3.0.3 #instalar antes de bokeh
pip install bokeh

import bokeh.io
bokeh.io.output_notebook()

from bokeh.plotting import figure, output_file, show
from bokeh.palettes import magma
import pandas as pd


#scatter plot
data_clean.info()
graph = figure(title="Gráfica de dispersión usando Bokeh")
#color=magma(256) #color
graph.scatter(x=data_clean["Edad"], y=data_clean["Gasto"]) #, color=color
show(graph) # ver gráfica


#line chart
graph= figure(title="Gráfica de barras con Bokeh") #título de la gráfica
df=data_clean["ENTIDAD"].value_counts() #count of each value of "ENTIDAD" column
graph.line(df, data_clean["ENTIDAD"]) #plotting the graph
show(graph) #ver gráfica

#bar chart
graph = figure(title="Gráfica de varras con Bokeh")
graph.vbar(data_clean["Gasto"], width=1, top=data_clean["Edad"]) # plotting the graph
show(graph) # ver gráfica

# visualización interactiva

from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import Title


#importación de librerías
import plotly.express as px
import pandas as pd
 
 
#############################################
#Gráficos interactivos
#pip install cufflinks






































































































