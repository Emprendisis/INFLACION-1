# Banxico SIE API – Inflación anual (SP30578)

Este repositorio descarga la serie de Banxico **Inflación anual (INPC, variación % anual)** usando la **SIE API**.

- Serie: `SP30578`
- Formato respuesta: JSON
- Autenticación: Token (header `Bmx-Token`)

## Estructura
- `src/banxico_client.py` – cliente reusable
- `src/download_inflacion.py` – descarga y exporta CSV
- `src/streamlit_app.py` – dashboard simple (opcional)
- `requirements.txt`

## Requisitos
- Python 3.10+
- Token Banxico SIE API

## Configuración del token (recomendado)
Crear variable de entorno:

**Windows (PowerShell)**
```powershell
setx BMX_TOKEN "TU_TOKEN_AQUI"
```

**macOS / Linux**
```bash
export BMX_TOKEN="TU_TOKEN_AQUI"
```

## Uso – descargar a CSV
```bash
pip install -r requirements.txt
python -m src.download_inflacion --out data/inflacion_anual_sp30578.csv
```

## Uso – Streamlit
```bash
streamlit run src/streamlit_app.py
```

## Nota
Si Banxico retorna `"N/E"` en algunos puntos, el script los convierte a `NaN`.
