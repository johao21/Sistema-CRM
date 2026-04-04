from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def inicio():
    return {"mensaje": "Backend CRM funcionando"}

@app.get("/leads", response_model=list[schemas.LeadResponse])
def listar_leads(db: Session = Depends(get_db)):
    return db.query(models.Lead).all()

@app.post("/leads", response_model=schemas.LeadResponse)
def crear_lead(lead: schemas.LeadCreate, db: Session = Depends(get_db)):
    nuevo_lead = models.Lead(
        nombre=lead.nombre,
        telefono=lead.telefono,
        correo=lead.correo,
        servicio=lead.servicio,
        estado_id=lead.estado_id,
        notas_generales=lead.notas_generales
    )
    db.add(nuevo_lead)
    db.commit()
    db.refresh(nuevo_lead)
    return nuevo_lead
from sqlalchemy import text

@app.get("/debug-estados")
def debug_estados(db: Session = Depends(get_db)):
    filas = db.execute(text("SELECT id, nombre FROM estados ORDER BY id")).fetchall()
    return [dict(f._mapping) for f in filas]