

import json
from schemas import InputSchema, OutputSchema
from rich import print


def procesar_request(json_string: str) -> dict:

    # 1 parsear JSON
    data = json.loads(json_string)

    # 2 validar con pydantic
    input_data = InputSchema(**data)

    # 3 lógica simple
    resultado = OutputSchema(
        year=input_data.year,
        industry=input_data.industry,
        variable=input_data.variable,
        value=input_data.value,
        status="ok"
    )

    return resultado.model_dump()


def main():

    json_request = """
    {
        "year": 2024,
        "industry": "manufacturing",
        "variable": "revenue",
        "value": 12000
    }
    """

    respuesta = procesar_request(json_request)

    print("[bold green]Respuesta de la API[/bold green]")
    print(respuesta)


if __name__ == "__main__":
    main()