
from typing import Callable
from functools import wraps
import time
import pandas as pd
import json
from rich import print

# funciones de limpieza
from limpieza import limpiar_columnas, eliminar_duplicados, manejar_faltantes

# esquemas Pydantic
from schemas import InputSchema, OutputSchema


# ------------------------------------------------
# Decorador para medir tiempo
# ------------------------------------------------

def medir_tiempo(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio: float = time.time()
        resultado = func(*args, **kwargs)
        fin: float = time.time()
        print(f"[cyan]Tiempo de ejecución:[/cyan] {fin - inicio:.4f} segundos")
        return resultado
    return wrapper


# ------------------------------------------------
# Ejemplo simple con type hinting
# ------------------------------------------------

@medir_tiempo
def suma(a: int, b: int) -> int:
    return a + b


# ------------------------------------------------
# Ruta del dataset
# ------------------------------------------------

RUTA_DATOS: str = r"C:\Users\juanf\Downloads\annual-enterprise-survey-2024-financial-year-provisional.csv"


# ------------------------------------------------
# Cargar datos
# ------------------------------------------------

@medir_tiempo
def cargar_datos(ruta: str) -> pd.DataFrame:

    df: pd.DataFrame = pd.read_csv(
        ruta,
        sep=",",
        encoding="latin-1"
    )

    print("\n[green]Datos cargados correctamente[/green]")
    print(f"Filas: {df.shape[0]} | Columnas: {df.shape[1]}")

    return df


# ------------------------------------------------
# Validar datos faltantes
# ------------------------------------------------

@medir_tiempo
def validar_datos_faltantes(df: pd.DataFrame) -> pd.Series:

    faltantes: pd.Series = df.isnull().sum()

    print("\n[yellow]Valores faltantes por columna:[/yellow]")
    print(faltantes)

    return faltantes


# ------------------------------------------------
# Estadística descriptiva
# ------------------------------------------------

@medir_tiempo
def estadistica_descriptiva(df: pd.DataFrame) -> pd.DataFrame:

    descripcion: pd.DataFrame = df.describe(include="all")

    print("\n[magenta]Estadística descriptiva[/magenta]")
    print(descripcion)

    return descripcion


# ------------------------------------------------
# Parsear JSON
# ------------------------------------------------

@medir_tiempo
def parsear_json(json_string: str) -> dict:

    datos: dict = json.loads(json_string)

    print("\n[blue]JSON parseado correctamente[/blue]")

    return datos


# ------------------------------------------------
# Validar con Pydantic
# ------------------------------------------------

@medir_tiempo
def validar_con_pydantic(data: dict) -> InputSchema:

    registro = InputSchema(**data)

    print("\n[green]Registro validado con Pydantic[/green]")

    return registro


# ------------------------------------------------
# Generar respuesta tipo API
# ------------------------------------------------

@medir_tiempo
def generar_respuesta(registro: InputSchema) -> dict:

    respuesta = OutputSchema(
        year=registro.year,
        industry_name_nzsioc=registro.industry_name_nzsioc,
        variable_name=registro.variable_name,
        value=registro.value
    )

    print("\n[bold green]Respuesta generada[/bold green]")

    return respuesta.model_dump()


# ------------------------------------------------
# MAIN
# ------------------------------------------------

def main() -> None:

    print("\n[bold cyan]Inicio del pipeline de datos[/bold cyan]\n")

    # Ejemplo simple
    resultado: int = suma(5, 3)
    print(f"Resultado suma: {resultado}")

    # 1️⃣ Cargar dataset
    df: pd.DataFrame = cargar_datos(RUTA_DATOS)

    # 2️⃣ Validar faltantes
    validar_datos_faltantes(df)

    # 3️⃣ Limpieza usando funciones externas
    df = limpiar_columnas(df)

    print("\nColumnas después de normalizar:")
    print(df.columns.tolist())

    df = eliminar_duplicados(df)

    print(f"\nFilas después de eliminar duplicados: {df.shape[0]}")

    df = manejar_faltantes(df)

    print("\nValores faltantes después de limpieza:")
    print(df.isnull().sum())

    # 4️⃣ Mostrar primeras filas
    print("\nPrimeras filas del dataset limpio:")
    print(df.head())

    # 5️⃣ Estadística descriptiva
    estadistica_descriptiva(df)

    # ------------------------------------------------
    # SEMANA 2 – SIMULACIÓN API
    # ------------------------------------------------

    print("\n[bold cyan]Simulación de API manual[/bold cyan]")

    # Tomar una fila del dataset
    fila: dict = df.iloc[0].to_dict()

    # Convertir a JSON
    json_string: str = json.dumps(fila)

    # Parsear JSON
    datos_parseados = parsear_json(json_string)

    # Validar con Pydantic
    registro_validado = validar_con_pydantic(datos_parseados)

    # Generar respuesta tipo API
    respuesta_api = generar_respuesta(registro_validado)

    print("\n[bold yellow]Respuesta final de la API[/bold yellow]")
    print(respuesta_api)


if __name__ == "__main__":
    main()