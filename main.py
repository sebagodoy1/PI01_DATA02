from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from databases import Database

database = Database("sqlite:///formula1.db")


#Creamos la variable app que será una instancia de la clase FastAPI
app = FastAPI()

#Generamos el mensaje de home/inicio
@app.get('/')
def home():
    return {"Data sobre F1"}



@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()

@app.get("/Año con más carreras")
async def fetch_data(id: int):
    consulta = "SELECT year, count(raceId) AS carreras FROM races GROUP BY year ORDER BY carreras DESC LIMIT 1".format(str(id))
    results = await database.fetch_all(query=consulta)
    return  results


@app.get("/Piloto con mayor cantidad de primeros puestos")
async def fetch_data(id: int):
    consulta = "SELECT r.driverId ,surname,forename, count(r.position) FROM results r JOIN drivers d ON r.driverId = d.driverId WHERE Position = 1".format(str(id))
    results = await database.fetch_all(query=consulta)
    return  results


@app.get("/Nombre del circuito más corrido")
async def fetch_data(id: int):
    consulta = "SELECT name, count(raceId) as carreras FROM races GROUP BY name ORDER BY carreras DESC LIMIT 1".format(str(id))
    results = await database.fetch_all(query=consulta)
    return  results


@app.get("/Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British")
async def fetch_data(id: int):
    consulta = "SELECT d.forename, d.surname ,r.driverId, sum(r.points) as puntaje_total FROM results r JOIN drivers d on r.driverId = d.driverId JOIN constructors c on r.constructorId = c.constructorId WHERE c.nationality = 'British' or c.nationality = 'American' GROUP BY r.driverId ORDER BY puntaje_total DESC LIMIT 1".format(str(id))
    results = await database.fetch_all(query=consulta)
    return  results
