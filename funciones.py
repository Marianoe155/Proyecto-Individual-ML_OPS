import pandas as pd
import numpy as np
import pickle

df1 = pd.read_parquet("clean_steam_games")
df2 = pd.read_parquet("clean_review")
# df3 = pd.read_parquet("clean_items")  LA LECTURA AL DATA SET DE ITEMS ME IMPIDE QUE FUNCIENE MI RENDER, DEBIDO QUE SOLO DISPONEMOS DE 500 DE RAM
# df_marge_item = pd.merge(df1, df3,on="item_id" ) #tabla de steam junto con item

df_merge_review = pd.merge(df1 ,df2, on="item_id") #tabla de steam junto con review

merge_ML = df_merge_review[["user_id","recommend","sentiment_analysis","app_name"]] #selecciono las columnas para el ML

#funcion N1

df_f1 = df1[["item_id", "price","developer","Año_lanzamiento"]] #tabla que utilizo en la funcion 1

def developer_(desarrollador):
    df_deve = df_f1[df_f1["developer"] == desarrollador] #llamo al desarrollador
    
    cant_item = df_deve.groupby("Año_lanzamiento")["item_id"].count() #obtengo la cantidad por año 
    
    Free = df_deve[df_deve["price"] == 0] #juegos gratuitos del desarrollador
    
    total_free = Free.groupby("Año_lanzamiento")["price"].count() #cantidad de gratis por año 

    cont_free_año = round((total_free/cant_item)*100,2) #porcentaje por free por año 
    
    #asigno nombre a las series
    cant_item.name = "Cantidad de Items"
    
    cont_free_año.name = "Contenido Free"
    
    tabla = pd.merge(cant_item, cont_free_año,on="Año_lanzamiento").reset_index() #unimos las dos tablas para hacerla unica
    tabla = tabla.fillna(0)
    tabla["Contenido Free"] = tabla["Contenido Free"].apply(lambda x: f"{x}%" if not pd.isna(x) else x)

    #Se renombra la columna "release_year":
    tabla = tabla.rename(columns={"release_year" : "Año"})

    return tabla


#funcion N2

df_f2 = df_merge_review[["user_id","price","recommend","item_id"]]
def userdata_(User_id):

    # Filtrar los datos para el usuario especificado
    user_data = df_f2[df_f2["user_id"] == User_id]

    #user_items = df3[df3["user_id"] == User_id]

    # Calcular la cantidad de dinero gastado por el usuario
    dinero_gastado = round(user_data["price"].sum(),2)

    # Calcular el porcentaje de recomendación en base a reviews.recommend
    recomendacion = user_data["recommend"].sum()
    
    porcentaje_recomendacion = round(recomendacion / len(user_data) * 100)

    # Calcular la cantidad de items
    cantidad_de_items = df_f2[df_f2["user_id"] == User_id]["item_id"].count() #no utilizo la tabla items por que es demasiada pesada
                        #user_items["item_id"].nunique()

    # Crear un diccionario con los resultados
    resultados = {f"Usuario X:{User_id}, Dinero gastado: {dinero_gastado}USD, % de recomendación: {porcentaje_recomendacion}%, Cantidad de items: {cantidad_de_items}"}
    return resultados

#funcion N3

### La funcion N3 no me funciona en el render, porque necesito cargar el dataframe de itmems y ocupa mas de 500mb de memoria ram 
### Pero de manera local en fastapi funciona
"""
df_f3 = df_marge_item.drop(columns=["item_id","app_name","price","developer","items_count","item_name"]) #tabla que utilizo en la funcion 3

def UserForGenre_(genero):
    df_genre = df_f3[df_f3[genero] == 1] #llamo el genero
    
    usur_mas_horas = df_genre.groupby("user_id")["playtime_forever"].sum().idxmax() #usuario con más horas de juego en el genero

    filtro_usur = df_genre[df_genre["user_id"] == usur_mas_horas] #filtramos por el usuario con mas horas jugadas

    horas_jugXaño = filtro_usur.groupby("Año_lanzamiento")["playtime_forever"].sum() #horas jugadas por año 

    registro = horas_jugXaño.to_dict() #paso las horas por año en diccionario

    Horas_por_año = {}  #creo un diccionario vacio para guardar registros 
    for clave, valor in registro.items(): #un for para que vaya iterando por cada item
        clave_formateada = f'Año: {int(clave)}' #formateo para que me salga con año
        valor_formateado = f'Horas: {int(valor)}' #formateo para que me salga con horas
        Horas_por_año[clave_formateada] = valor_formateado 

    return f"Usuario con más horas jugadas para Género {genero} : {usur_mas_horas}, Horas jugadas:{Horas_por_año}"
"""
#funcion N4

df_f4 = df_merge_review[["Año_posteo","recommend","sentiment_analysis","developer","app_name"]] 

def best_developer_year_(año):

    # Filtrar los juegos por año
    df_año = df_f4[df_f4["Año_posteo"] == año]

    # Agrupar los juegos por desarrollador y contar el número de juegos recomendados
    df_count = df_año[df_año["recommend"] == True][df_año["sentiment_analysis"] == 2].groupby("developer")["app_name"].count().reset_index()

    # Ordenar los resultados por número de juegos recomendados y devolver los tres primeros desarrolladores
    top_desarrolladores = df_count.sort_values("app_name", ascending=False).head(3)["developer"].tolist()

    # Devolver el top 3 de desarrolladores
    return f"Puesto1:{top_desarrolladores[0]}, Puesto2:{top_desarrolladores[1]}, Puesto3:{top_desarrolladores[2]}"

#funcion N5

def developer_reviews_analysis_(developer):
    '''Devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de 
    reseñas positivas y negativas de usuarios

    Ejemplo de retorno: {'Valve' : [Negative = 182, Positive = 278]}
    '''

    # Se filtran las columnas a utilizar y se eliminan duplicados
    df_merged = df_merge_review[["user_id", "item_id","developer","Año_posteo","sentiment_analysis"]]

    #Se filtran los datos por el developer ingresado
    df_merged = df_merged[df_merged["developer"] == developer]

    # Se obtienen la cantidad de reviews positivas y negativas
    positive_reviews = df_merged[df_merged["sentiment_analysis"] == 2].shape[0]
    negative_reviews = df_merged[df_merged["sentiment_analysis"] == 0].shape[0]

    #Se juntan los valores en un f-string
    resumen_reviews = f"[Negative = {negative_reviews}, Positive = {positive_reviews}]"

    #Se almacenan los resultados en un diccionario
    dicc = {developer : resumen_reviews}

    # Se devuelve un diccionario con los resultados obtenidos
    return dicc

#funcion_de_ML N6 
with open ("modelo_de_ML.pkl", "rb") as archivo: # abro el archivo donde tengo guardado el modelo de ML
    modelo_pickle = pickle.load(archivo)

def recomendacion_usuario_(id_usuario):
    if not (merge_ML["user_id"] == id_usuario).any():
        return {f"El usuario {id_usuario} no está en el data set."}
    else:
    # Veo los juegos jugados por el usuario
        juegos_jugados = merge_ML[merge_ML["user_id"] == id_usuario]["app_name"].unique()

    # Guardo todos los juegos en una variable
        juegos = merge_ML["app_name"].unique()
    
    # Crear una lista de juegos no valorados por el usuario específico
        juegos_no_jugados = list(set(juegos) - set(juegos_jugados))

    # Hacemos predicciones de los juegos no jugados por el usuario
        predic_no_jugados = [modelo_pickle.predict(id_usuario, linea) for linea in juegos_no_jugados]

    # Ordeno la prediccion de acuerdo a su respectiva valoración y obtengo los 5 primeros
        Top5_recomm = sorted(predic_no_jugados, key=lambda x: x.est, reverse=True)[:5] 

    # Coloco los juegos recomendados en una lista
        lista_juegos = []
        for recomendacion in Top5_recomm:
            lista_juegos.append(recomendacion.iid)

    # 5 juegos de recomendacion
        return {f"Juego 1:{lista_juegos[0]}, Juego 2:{lista_juegos[1]}, Juego 3:{lista_juegos[2]}, Juego 4:{lista_juegos[3]}, Juego 5:{lista_juegos[4]}"}

    

