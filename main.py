#Comenzamos importando librerías necesarias
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from databases import Database

#Imporamos la db de sqlite
database = Database("sqlite:///formula1.db")


#Creamos la variable app que será una instancia de la clase FastAPI
app = FastAPI()

#Generamos el mensaje de home/inicio
@app.get('/')
def home():
    return {"Data sobre F1"}


#Activamos la DB
@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


#1° consulta requerida
@app.get("/Año con más carreras")
async def fetch_data(Quantity: int):
    consulta = "SELECT year, count(raceId) AS carreras FROM races GROUP BY year ORDER BY carreras DESC LIMIT {}".format(str(Quantity))
    results = await database.fetch_all(query=consulta)
    return  results


#2° consulta requerida
@app.get("/Piloto con mayor cantidad de primeros puestos")
async def fetch_data(Quantity: int):
    consulta = "SELECT r.driverId ,surname,forename, count(r.position) FROM results r JOIN drivers d ON r.driverId = d.driverId WHERE Position = 1 GROUP BY r.driverId ORDER BY count(r.position) DESC LIMIT {}".format(str(Quantity))
    results = await database.fetch_all(query=consulta)
    return  results


#3° consulta requerida
@app.get("/Nombre del circuito más corrido")
async def fetch_data(Quantity: int):
    consulta = "SELECT c.name, count(raceId) as carreras   FROM races  r join circuits c on c.circuitId = r.circuitId GROUP BY c.name ORDER BY carreras DESC LIMIT {}".format(str(Quantity))
    results = await database.fetch_all(query=consulta)
    return  results

#4° consulta requerida
@app.get("/Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British")
async def fetch_data(Quantity: int):
    consulta = "SELECT d.forename, d.surname ,r.driverId, sum(r.points) as puntaje_total FROM results r JOIN drivers d on r.driverId = d.driverId JOIN constructors c on r.constructorId = c.constructorId WHERE c.nationality = 'British' or c.nationality = 'American' GROUP BY r.driverId ORDER BY puntaje_total DESC LIMIT {}".format(str(Quantity))
    results = await database.fetch_all(query=consulta)
    return  results
