# Listado, Adicionar, Eliminar, Consultar por Id, Actualizar por Id para 5 tablas de su base de datos.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/hotel_correcto"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()