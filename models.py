from sqlalchemy import Column, Integer, Float, String, DateTime, func
from database import Base

class Bus(Base):
    __tablename__= "buses"
    
    id= Column(Integer, primary_key= True, index= True)
    hora = Column(DateTime, default=func.now())
    latitud= Column(Float, nullable=False)
    longitud= Column(Float, nullable=False)
    nombre= Column(String, nullable=False)