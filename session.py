# Listado, Adicionar, Eliminar, Consultar por Id, Actualizar por Id para 5 tablas de su base de datos.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:@localhost:5432/123"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()