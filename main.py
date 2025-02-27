from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import engine, Base, get_db
from models import Bus

import os
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI()

class BusData(BaseModel):
    latitud: float
    longitud: float
    nombre: str

@app.post("/actualizar_ubicacion/")
def actualizar_ubicacion(bus_data: BusData, db: Session = Depends(get_db)):
    bus = Bus(latitud=bus_data.latitud, longitud=bus_data.longitud, nombre=bus_data.nombre)
    db.add(bus)
    db.commit()
    return {"mensaje": "Ubicación actualizada"}

#Utilizado para poder enviar datos escritos por la WEB FastAPI

#@app.post("/actualizar_ubicacion/")
#def actualizar_ubicacion(
#    latitud: float, 
#    longitud: float, 
#    nombre: str, 
#    db: Session = Depends(get_db)):
#    bus = Bus(latitud=latitud, longitud=longitud, nombre=nombre) 
#    db.add(bus)
#    db.commit()
#    return {"mensaje": "Ubicación actualizada"}

@app.get("/buses/")
def obtener_buses(db: Session = Depends(get_db)):
    return db.query(Bus).all()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringirlo a ["http://localhost"] si lo deseas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API funcionando"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Usa el puerto asignado por Railway
    uvicorn.run(app, host="0.0.0.0", port=port)