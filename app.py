from flask import Flask, request, jsonify
import pandas as pd

# importar funciones de limpieza (Semana 1)
from limpieza import limpiar_columnas, eliminar_duplicados, manejar_faltantes

app = Flask(__name__)


# -----------------------------------------
# Endpoint 1
# GET /
# -----------------------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "mensaje": "API de limpieza de datos activa",
        "endpoints": {
            "status": "/status",
            "clean": "POST /clean"
        }
    })


# -----------------------------------------
# Endpoint 2
# GET /status
# -----------------------------------------
@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "status": "API funcionando correctamente"
    })


# -----------------------------------------
# Endpoint 3
# POST /clean
# Recibe JSON y limpia datos
# -----------------------------------------
@app.route("/clean", methods=["POST"])
def clean_data():

    # verificar que venga JSON
    if not request.is_json:
        return jsonify({
            "error": "El request debe ser JSON",
            "solucion": "Enviar header Content-Type: application/json"
        }), 415

    data = request.get_json()

    try:

        # convertir a DataFrame
        df = pd.DataFrame(data)

        # aplicar funciones de limpieza
        df = limpiar_columnas(df)
        df = eliminar_duplicados(df)
        df = manejar_faltantes(df)

        return jsonify({
            "mensaje": "Datos limpiados correctamente",
            "filas_resultado": len(df),
            "columnas": list(df.columns),
            "preview": df.head(10).to_dict(orient="records")
        })

    except Exception as e:

        return jsonify({
            "error": "Error procesando los datos",
            "detalle": str(e)
        }), 500


# -----------------------------------------
# Ejecutar servidor
# -----------------------------------------
if __name__ == "__main__":
    app.run(debug=True)