from typing import Union
from fastapi import FastAPI
from funciones import developer_reviews_analysis_,developer_,best_developer_year_ #,userdata_,UserForGenre_,best_developer_year_
from fastapi.responses import JSONResponse 

app= FastAPI()
"""
@app.get("/")
async def root():
    return {"message":"Hello world"}

@app.get("/items/{item_id}")
def read_item (item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
"""
#funcion N1

@app.get("/developer/{desarrollador}")
async def developer(desarrollador: str):
        contenido_Free = developer_(desarrollador)
            # Devolver el resultado como respuesta JSON
        return JSONResponse(contenido_Free.to_dict(orient="records"))
"""
#funcion N2

@app.get("/userdata/{Userd_id}")
async def userdata( User_id : str ):
    usuario = userdata_(User_id)
    return usuario

#funcion N3

@app.get("/UserForGenre/{genero}")
async def UserForGenre(genero: str):
    Horas_por_año = UserForGenre_(genero)
    return Horas_por_año
"""
#funcion N4

@app.get("/best_developer_year/{year}")
async def Best_developer_year(year: str):
    try:
        year_int = int(year)  # Convertir el año a un entero
        result2 = best_developer_year_(year_int)
        return result2
    except Exception as e:
        return {"error": str(e)}

#funcion N5

@app.get("/developer_reviews_analysis/{developer}")
async def developer_reviews_analysis(developer: str):
    Reseñas = developer_reviews_analysis_(developer)
    return Reseñas



