import pandas as pd


def limpiar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza los nombres de las columnas.
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
    )
    return df


def eliminar_duplicados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina filas duplicadas del dataset.
    """
    df = df.copy()
    return df.drop_duplicates()


def manejar_faltantes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Manejo básico de valores faltantes.
    - Numéricos → mediana
    - Categóricos → 'desconocido'
    """
    df = df.copy()

    for col in df.select_dtypes(include="number"):
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include="object"):
        df[col] = df[col].fillna("desconocido")

    return df


def limpieza_basica(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pipeline de limpieza básica.
    """
    df = limpiar_columnas(df)
    df = eliminar_duplicados(df)
    df = manejar_faltantes(df)
    return df