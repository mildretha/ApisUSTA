from fastapi import FastAPI
import pandas as pd
from typing import List, Dict

# funciones de limpieza (Semana 1)
from limpieza import limpiar_columnas, eliminar_duplicados, manejar_faltantes

# crear aplicación
app = FastAPI(
    title="API Limpieza de Datos",
    description="API creada en FastAPI para limpiar datasets usando funciones de Pandas",
    version="1.0"
)


# --------------------------------
# Endpoint 1
# --------------------------------
@app.get("/")
def home():
    return {
        "mensaje": "API de limpieza de datos activa",
        "endpoints": {
            "status": "/status",
            "clean": "/clean"
        }
    }


# --------------------------------
# Endpoint 2
# --------------------------------
@app.get("/status")
def status():
    return {
        "status": "API funcionando correctamente"
    }


# --------------------------------
# Endpoint 3
# Limpieza de datos
# --------------------------------
@app.post("/clean")
def clean_data(data: List[Dict]):

    # convertir JSON a DataFrame
    df = pd.DataFrame(data)

    # aplicar limpieza
    df = limpiar_columnas(df)
    df = eliminar_duplicados(df)
    df = manejar_faltantes(df)

    return {
        "mensaje": "Datos limpiados correctamente",
        "filas_resultado": len(df),
        "columnas": list(df.columns),
        "preview": df.head(10).to_dict(orient="records")
    }